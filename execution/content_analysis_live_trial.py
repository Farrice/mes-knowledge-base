#!/usr/bin/env python3
"""Qualified fixed-source static Gemini trial. No automatic retries or general allowance."""
import argparse
import fcntl
import json
import os
import time
import urllib.error
import urllib.request
from pathlib import Path
from content_analysis_pilot import Denied, canonical, digest, shared_state_dir, PRICE_EXPIRY

JOB = 'creative-strategist-z2uoa3bhjt0'
URI = 'https://www.youtube.com/watch?v=Z2uoA3bhJT0'
RESERVATION = 1_250_000
MAX_CALLS = 6
AUTH = 'Farrice approved full-video Gemini test and extraction, total USD 10, 2026-09-14'


def payload(question, start=0, end=9908):
    if not isinstance(question,str) or not 1 <= len(question) <= 12000:
        raise Denied('question length invalid')
    if type(start) is not int or type(end) is not int or not 0 <= start < end <= 9908:
        raise Denied('invalid source interval')
    return {'model':'gemini-3.8-flash','store':False,'background':False,
            'input':[{'type':'video','uri':URI,'resolution':'low',
                      'processing':{'type':'static','fps':1,'start_offset':f'{start}s','end_offset':f'{end}s'}},
                     {'type':'text','text':question}],
            'generation_config':{'max_output_tokens':16384,'thinking_level':'low','tool_choice':'none'}}


def validate(p):
    try:
        v,t=p['input']; start=int(v['processing']['start_offset'][:-1]);end=int(v['processing']['end_offset'][:-1])
        if p != payload(t['text'],start,end): raise ValueError()
    except (KeyError,TypeError,ValueError): raise Denied('request differs from qualified static envelope')
    if time.time() >= PRICE_EXPIRY: raise Denied('pricing expired')


def atomic(path,data):
    tmp=path.with_suffix('.tmp')
    with tmp.open('w') as f:
        f.write(json.dumps(data,indent=2));f.flush();os.fsync(f.fileno())
    os.replace(tmp,path)


def usage_receipt(response):
    u=response.get('usage')
    if not isinstance(u,dict) or any(type(u.get(k)) is not int or u[k]<0 for k in ['total_input_tokens','total_output_tokens','total_tokens']):
        raise Denied('missing usage; reservation retained, further calls blocked')
    if response.get('status') != 'completed':
        raise Denied('provider response not completed; retain reservation')
    if u['total_tokens'] < u['total_input_tokens'] + u['total_output_tokens']:
        raise Denied('inconsistent usage counters; independent reconciliation required')
    if u['total_input_tokens'] == 0 and (u.get('raw_prompt_token',0) or u.get('model_invocation_token_counts')):
        raise Denied('conflicting input counters; independent reconciliation required')
    # Bill all non-input tokens at output price: deliberately conservative including thoughts.
    cost=(u['total_input_tokens']*.75+max(u['total_output_tokens'],u['total_tokens']-u['total_input_tokens'])*3.75)/1e6
    if u.get('total_tool_use_tokens',0) or cost>RESERVATION/1e6:
        raise Denied('usage exceeds qualified envelope; stop')
    return {'usage':u,'conservative_usage_cost_usd':round(cost,6),'invoice_status':'NOT_VERIFIED'}


def run(p,authorization,root=None,transport=None):
    validate(p)
    if authorization != AUTH: raise Denied('explicit job authorization required')
    root=Path(root) if root else shared_state_dir()/'live-trials'/JOB
    root.mkdir(parents=True,exist_ok=True)
    with (root/'single-flight.lock').open('a') as lock:
        try: fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError: raise Denied('another request is running')
        statepath=root/'ledger.json'; key=digest(p)
        state=json.loads(statepath.read_text()) if statepath.exists() else {'job':JOB,'authorization':AUTH,'cap_micro_usd':10_000_000,'calls':[]}
        if state['job']!=JOB or state['authorization']!=AUTH or state['cap_micro_usd']!=10_000_000: raise Denied('ledger invalid')
        for c in state['calls']:
            if c['status']!='complete': raise Denied('unresolved attempt; no retry or new dispatch')
            if c['key']==key: return {'cached':True,'receipt':c,'root':str(root)}
        if len(state['calls'])>=MAX_CALLS or sum(c['reserved_micro_usd'] for c in state['calls'])+RESERVATION>7_500_000:
            raise Denied('qualified job request allowance exhausted')
        c={'key':key,'status':'reserved','reserved_micro_usd':RESERVATION,'created':time.time(),'request':p}
        state['calls'].append(c);atomic(statepath,state)
        try:
            if transport is None:
                from dotenv import dotenv_values
                env=dotenv_values(Path(__file__).resolve().parents[1]/'.env');secret=env.get('GEMINI_API_KEY')
                if not secret: raise Denied('configured Gemini key unavailable')
                req=urllib.request.Request('https://generativelanguage.googleapis.com/v1beta/interactions',data=canonical(p).encode(),headers={'Content-Type':'application/json','x-goog-api-key':secret})
                # urllib performs no application retries. HTTP deadline is not remote cancellation.
                with urllib.request.urlopen(req,timeout=600) as r: result=json.load(r)
            else: result=transport(p)
            atomic(root/(key+'.response.json'),result)
            c.update(usage_receipt(result));c.update(status='complete',completed=time.time(),provider_status=result.get('status'),response_file=key+'.response.json')
            atomic(statepath,state)
            return {'cached':False,'receipt':c,'root':str(root)}
        except urllib.error.HTTPError as e:
            # Persist only error body, never request headers/key. Do not retry denied calls.
            detail=e.read().decode('utf-8',errors='replace');atomic(root/(key+'.error.json'),{'http_status':e.code,'body':detail})
            c.update(status='rejected' if e.code in (400,401,403,404,429) else 'unknown',http_status=e.code,error_file=key+'.error.json');atomic(statepath,state)
            raise Denied(f'HTTP {e.code}; attempt preserved; no automatic retry') from None
        except BaseException as e:
            c.update(status='unknown',error_type=type(e).__name__);atomic(statepath,state)
            raise


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('request',type=Path);ap.add_argument('--authorization',required=True);a=ap.parse_args()
    try: print(json.dumps(run(json.loads(a.request.read_text()),a.authorization),indent=2))
    except (Denied,OSError,ValueError) as e: print(json.dumps({'status':'STOPPED','reason':str(e)}));return 1
    return 0
if __name__=='__main__': raise SystemExit(main())
