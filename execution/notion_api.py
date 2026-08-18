#!/usr/bin/env python3
"""
Notion API wrapper — pins to Notion-Version 2022-06-28.

Why?
@notionhq/client v5.9.0 uses a newer API that breaks database property
handling (returns "data_sources" instead of "properties"). Pinning to
2022-06-28 restores full property support.

Usage:
    from execution.notion_api import NotionAPI
    api = NotionAPI()  # reads NOTION_API_KEY from .env
    api.create_page("database-id", {"Name": api.title("My Page"), ...})

CLI usage:
    python execution/notion_api.py query <database_id>
    python execution/notion_api.py search <query>
    python execution/notion_api.py capture "Title" "Content" --type Task --tags Revenue,Urgent
"""

import os
import json
import argparse
import requests
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlencode
from dotenv import load_dotenv

# Load .env — jarvis-bot first (has Notion keys), then root as fallback
# load_dotenv doesn't override existing vars, so order matters
for env_path in [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]:
    if env_path.exists():
        load_dotenv(env_path)

NOTION_VERSION = '2022-06-28'
BASE_URL = 'https://api.notion.com/v1'

# Database IDs from environment
DB_IDS = {
    'projects':       os.getenv('NOTION_DB_PROJECTS', ''),
    'knowledge':      os.getenv('NOTION_DB_KNOWLEDGE', ''),
    'content':        os.getenv('NOTION_DB_CONTENT', ''),
    'captures':       os.getenv('NOTION_DB_CAPTURES', ''),
    'personal':       os.getenv('NOTION_DB_PERSONAL', ''),
    # Shared Riley Brown / Social Intelligence content bank.  Video evidence
    # packets from /watch upsert here rather than creating a second database.
    'social_intel':   os.getenv('NOTION_DB_SOCIAL_INTEL', ''),
    # Session Memory — the human-facing second-brain log (Simon Intellectual
    # Library, Phase 3). Created via Notion AI Prompt 1; set its id in .env.
    'session_memory': os.getenv('NOTION_DB_SESSION_MEMORY', ''),
}


class NotionAPIError(Exception):
    def __init__(self, status: int, code: str, message: str):
        super().__init__(message)
        self.status = status
        self.code = code


class NotionAPI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = (api_key or os.getenv('NOTION_API_KEY', '')).strip('"').strip("'")
        if not self.api_key:
            raise ValueError("NOTION_API_KEY not set")
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Notion-Version': NOTION_VERSION,
            'Content-Type': 'application/json',
        }

    def _request(self, method: str, path: str, body: Optional[dict] = None) -> dict:
        url = f'{BASE_URL}{path}'
        res = requests.request(method, url, headers=self.headers, json=body)
        data = res.json()
        if not res.ok:
            raise NotionAPIError(res.status_code, data.get('code', 'unknown'), data.get('message', f'HTTP {res.status_code}'))
        return data

    # ─── Database Operations ─────────────────

    def get_database(self, database_id: str) -> dict:
        return self._request('GET', f'/databases/{database_id}')

    def update_schema(self, database_id: str, properties: dict) -> dict:
        return self._request('PATCH', f'/databases/{database_id}', {'properties': properties})

    def query_database(self, database_id: str, filter: Optional[dict] = None, sorts: Optional[list] = None, page_size: int = 100) -> dict:
        body: dict[str, Any] = {'page_size': page_size}
        if filter:
            body['filter'] = filter
        if sorts:
            body['sorts'] = sorts
        return self._request('POST', f'/databases/{database_id}/query', body)

    # ─── Page Operations ─────────────────────

    def create_page(self, database_id: str, properties: dict, children: Optional[list] = None) -> dict:
        body: dict[str, Any] = {'parent': {'database_id': database_id}, 'properties': properties}
        if children:
            body['children'] = children
        return self._request('POST', '/pages', body)

    def update_page(self, page_id: str, properties: dict) -> dict:
        return self._request('PATCH', f'/pages/{page_id}', {'properties': properties})

    def list_block_children(self, block_id: str, start_cursor: Optional[str] = None, page_size: int = 100) -> dict:
        params: dict[str, Any] = {'page_size': page_size}
        if start_cursor:
            params['start_cursor'] = start_cursor
        return self._request('GET', f'/blocks/{block_id}/children?{urlencode(params)}')

    # ─── Search ──────────────────────────────

    def search(self, query: str, page_size: int = 10) -> dict:
        return self._request('POST', '/search', {
            'query': query,
            'page_size': page_size,
            'sort': {'direction': 'descending', 'timestamp': 'last_edited_time'},
        })

    # ─── Property Builders ───────────────────

    @staticmethod
    def title(text: str) -> dict:
        return {'title': [{'text': {'content': text}}]}

    @staticmethod
    def rich_text(text: str) -> dict:
        return {'rich_text': [{'text': {'content': text}}]}

    @staticmethod
    def select(name: str) -> dict:
        return {'select': {'name': name}}

    @staticmethod
    def multi_select(names: list[str]) -> dict:
        return {'multi_select': [{'name': n} for n in names]}

    @staticmethod
    def number(value: float) -> dict:
        return {'number': value}

    @staticmethod
    def date(start: str, end: Optional[str] = None) -> dict:
        d: dict[str, str] = {'start': start}
        if end:
            d['end'] = end
        return {'date': d}

    @staticmethod
    def checkbox(checked: bool) -> dict:
        return {'checkbox': checked}

    # ─── Block Builders (page BODY content, not properties) ──
    # Notion caps a single rich_text object at 2000 chars. For longer text we
    # split into multiple text runs within ONE block rather than multiple
    # blocks — keeps the body readable instead of fragmenting paragraphs.

    @staticmethod
    def _rich_text_runs(text: str, chunk: int = 1900) -> list[dict]:
        text = text or ''
        if not text:
            return [{'type': 'text', 'text': {'content': ''}}]
        return [
            {'type': 'text', 'text': {'content': text[i:i + chunk]}}
            for i in range(0, len(text), chunk)
        ] or [{'type': 'text', 'text': {'content': ''}}]

    @classmethod
    def heading2(cls, text: str) -> dict:
        return {
            'object': 'block', 'type': 'heading_2',
            'heading_2': {'rich_text': cls._rich_text_runs(text, 1900)},
        }

    @classmethod
    def para(cls, text: str) -> dict:
        return {
            'object': 'block', 'type': 'paragraph',
            'paragraph': {'rich_text': cls._rich_text_runs(text)},
        }

    @classmethod
    def bullet(cls, text: str) -> dict:
        return {
            'object': 'block', 'type': 'bulleted_list_item',
            'bulleted_list_item': {'rich_text': cls._rich_text_runs(text)},
        }

    # ─── Schema Helpers ───────────────────────
    # Process-lifetime cache so repeated calls in one script run don't
    # re-fetch the DB schema on every page creation.
    _schema_cache: dict[str, set] = {}

    def _ensure_properties(self, database_id: str, required: dict) -> set:
        """Ensure `required` (name -> Notion property-type spec) exist on the
        DB. Additive-only — NEVER changes the type of an existing property
        (verified experimentally: converting an existing property's type via
        PATCH silently discards its stored values on every row). Returns the
        set of property names now known-present. Degrades gracefully: if the
        PATCH fails (e.g. non-integration-owned DB), returns whatever was
        already present and callers should skip properties not in the set.
        """
        cached = self._schema_cache.get(database_id)
        if cached is None:
            try:
                db = self.get_database(database_id)
                cached = set(db.get('properties', {}).keys())
            except Exception:
                cached = set()
            self._schema_cache[database_id] = cached

        missing = {k: v for k, v in required.items() if k not in cached}
        if missing:
            try:
                self.update_schema(database_id, missing)
                cached = cached | set(missing.keys())
                self._schema_cache[database_id] = cached
            except Exception:
                pass  # degrade gracefully — property stays unavailable
        return cached

    # ─── High-Level Functions ────────────────

    def capture(self, name: str, raw_content: str, type: str = 'Note', source: str = 'Claude Code', tags: Optional[list[str]] = None) -> dict:
        from datetime import date
        props: dict[str, Any] = {
            'Name': self.title(name),
            'Type': self.select(type),
            'Source': self.select(source),
            'Processed': self.checkbox(False),
            'Raw Content': self.rich_text(raw_content),
            'Captured At': self.date(date.today().isoformat()),
        }
        if tags:
            props['Tags'] = self.multi_select(tags)
        return self.create_page(DB_IDS['captures'], props)

    def create_knowledge_vault_entry(
        self,
        name: str,
        source: str = 'Claude Code',
        expert: str = '',
        domain: str = '',
        entry_type: str = 'Research Brief',
        key_patterns: str = '',
        genius_score: Optional[int] = None,
        date_extracted: Optional[str] = None,
        antigravity_skill: str = '',
        tags: Optional[list[str]] = None,
        # ── Rich-body additions (2026-07) — all optional, all backward
        # compatible. `name` may now be a full "what was produced" summary;
        # the page TITLE becomes a short (~80 char) truncation of it, and the
        # full text goes into the page BODY so entries are human-readable
        # instead of one giant run-on header (Farrice complaint, 2026-07-06).
        summary: str = '',
        workflow: str = '',
        task_type: str = '',
        intent_score: Optional[float] = None,
        expert_score: Optional[float] = None,
        adversarial_score: Optional[float] = None,
        factual_score: Optional[float] = None,
        composite_score: Optional[float] = None,
        verdict: str = '',
        sub_agents: Optional[int] = None,
        notes: str = '',
        session_date: Optional[str] = None,
        include_git_info: bool = True,
        title_override: Optional[str] = None,
    ) -> str:
        """Create an entry in the Knowledge Vault database.

        Args:
            name: Entry title (required) — or, if `summary` is omitted, the
                full "what was produced" text (will be truncated for the
                page title; the full text still lands in the body).
            source: Where it came from (extraction, search, etc.).
            expert: Expert name if applicable.
            domain: Knowledge domain.
            entry_type: One of "MES 3.0 Extraction", "Research Brief", "Framework",
                        "Case Study", "Pattern Library", "Book Notes".
            key_patterns: Comma-separated key patterns.
            genius_score: 2-5 rating.
            date_extracted: ISO date string (defaults to today).
            antigravity_skill: Skill path if applicable.
            tags: List of tags like "Crown Jewel", "Hidden Knowledge",
                  "Actionable", "Reference".
            summary: Full "what was produced" text. If given, `name` is only
                used as a title hint; if omitted, `name` itself is treated
                as the summary and truncated for the title.
            workflow, task_type: Context fields for the body's Context section.
            intent_score, expert_score, adversarial_score, factual_score,
                composite_score: Quality Gate scores (1-10) for the Scores
                section. All optional — section is skipped if none given.
            verdict: 'PASS' | 'PARTIAL' | 'FAIL' — written to the Verdict
                select property (added to schema if missing) AND the body.
            sub_agents: Measured sub-agent spawn count for Context.
            notes: Freeform finalize notes — becomes the Notes section.
            session_date: ISO date for the body's Context section (defaults
                to date_extracted).
            include_git_info: Attempt a cheap `git rev-parse` for a Links
                section; silently skipped on any failure.
            title_override: If given, used verbatim as the page title instead
                of the auto-truncated summary.

        Returns:
            The Notion page URL of the created entry.
        """
        from datetime import date as _date

        if date_extracted is None:
            date_extracted = _date.today().isoformat()
        if session_date is None:
            session_date = date_extracted

        # Validate entry_type
        valid_types = {
            'MES 3.0 Extraction', 'Research Brief', 'Framework',
            'Case Study', 'Pattern Library', 'Book Notes',
        }
        if entry_type not in valid_types:
            raise ValueError(
                f"Invalid entry_type '{entry_type}'. Must be one of: {', '.join(sorted(valid_types))}"
            )

        # Validate genius_score if provided
        if genius_score is not None and not (2 <= genius_score <= 5):
            raise ValueError(f"genius_score must be 2-5, got {genius_score}")

        # Validate tags if provided
        valid_tags = {'Crown Jewel', 'Hidden Knowledge', 'Actionable', 'Reference'}
        if tags:
            bad_tags = set(tags) - valid_tags
            if bad_tags:
                raise ValueError(
                    f"Invalid tags: {bad_tags}. Must be from: {', '.join(sorted(valid_tags))}"
                )

        # Validate verdict if provided
        valid_verdicts = {'PASS', 'PARTIAL', 'FAIL'}
        if verdict and verdict not in valid_verdicts:
            raise ValueError(f"Invalid verdict '{verdict}'. Must be one of: {', '.join(sorted(valid_verdicts))}")

        full_summary = summary or name
        page_title = title_override or _short_title(full_summary)

        # Knowledge Vault database ID
        vault_db_id = DB_IDS.get('knowledge', '5c63b25c-e040-4c6f-8a7b-906643090694')
        if not vault_db_id:
            vault_db_id = '5c63b25c-e040-4c6f-8a7b-906643090694'

        # Build properties
        props: dict[str, Any] = {
            'Name': self.title(page_title),
            'Type': self.select(entry_type),
            'Date Extracted': self.date(date_extracted),
        }

        if source:
            props['Source'] = self.rich_text(source)
        if expert:
            props['Expert'] = self.rich_text(expert)
        if domain:
            props['Domain'] = self.rich_text(domain)
        if key_patterns:
            props['Key Patterns'] = self.rich_text(key_patterns)
        if genius_score is not None:
            props['Genius Score'] = self.number(genius_score)
        if antigravity_skill:
            props['Antigravity Skill'] = self.rich_text(antigravity_skill)
        if tags:
            props['Tags'] = self.multi_select(tags)

        # New filterable properties — additive schema only (never mutate an
        # existing property's type; see _ensure_properties docstring).
        degraded: list[str] = []
        if composite_score is not None or verdict:
            available = self._ensure_properties(vault_db_id, {
                'Verdict': {'select': {'options': [{'name': v} for v in sorted(valid_verdicts)]}},
                'Composite': {'number': {}},
            })
            if verdict:
                if 'Verdict' in available:
                    props['Verdict'] = self.select(verdict)
                else:
                    degraded.append('Verdict')
            if composite_score is not None:
                if 'Composite' in available:
                    props['Composite'] = self.number(composite_score)
                else:
                    degraded.append('Composite')

        git_branch, git_commit = ('', '')
        if include_git_info:
            git_branch, git_commit = _git_info()

        children = build_vault_body_blocks(
            full_summary,
            intent_score=intent_score, expert_score=expert_score,
            adversarial_score=adversarial_score, factual_score=factual_score,
            composite_score=composite_score, verdict=verdict,
            expert=expert, skill=antigravity_skill, workflow=workflow,
            entry_type=entry_type, task_type=task_type, sub_agents=sub_agents,
            session_date=session_date, notes=notes,
            git_branch=git_branch, git_commit=git_commit,
        )

        try:
            result = self.create_page(vault_db_id, props, children=children)
            url = result['url']
        except NotionAPIError as e:
            raise RuntimeError(
                f"Failed to create Knowledge Vault entry: [{e.status}] {e.code} — {e}"
            ) from e

        if degraded:
            # Non-fatal — page was created; surface which properties fell
            # back so callers can report it (see chain_runner call site).
            self._last_degraded = degraded
        else:
            self._last_degraded = []
        return url

    def push_session_memory(
        self,
        title: str,
        key_decisions: str,
        pickup_prompt: str = '',
        mode: str = 'Claude Code',
        date_str: Optional[str] = None,
    ) -> str:
        """Push ONE distilled session-memory row to the Notion second brain.

        ALLOW-LIST CONTRACT (privacy boundary, Phase 4): only these five fields
        ever leave the machine — Title, Date, Advisor/Mode, Key Decisions,
        Pickup Prompt. NEVER pass raw transcripts / assistant_message blobs here;
        client + personal content stays in the local stores. One-way local→Notion.

        Target: the Simon Intellectual Library "💬 Session Memory" DB
        (NOTION_DB_SESSION_MEMORY). Created via the Notion AI deployment pack at
        _active/knowledge/notion-intellectual-library/notion-ai-deployment-prompts.md.
        """
        from datetime import date as _date

        db_id = DB_IDS.get('session_memory', '')
        if not db_id:
            raise RuntimeError(
                "NOTION_DB_SESSION_MEMORY not set. Run Prompt 1 in "
                "_active/knowledge/notion-intellectual-library/notion-ai-deployment-prompts.md "
                "to create the Session Memory DB in Notion AI, then add its id to .env."
            )
        if date_str is None:
            date_str = _date.today().isoformat()
        # Notion rich_text caps at 2000 chars per text object — truncate defensively.
        props: dict[str, Any] = {
            'Title': self.title(title),
            'Date': self.date(date_str),
            'Advisor/Mode': self.rich_text(mode),
            'Key Decisions': self.rich_text((key_decisions or '')[:1900]),
            'Pickup Prompt': self.rich_text((pickup_prompt or '')[:1900]),
        }
        result = self.create_page(db_id, props)
        return result['url']


# ─── Knowledge Vault body helpers (module-level; also used by
# execution/notion_backfill_knowledge.py to reconstruct existing empty pages
# in the same layout) ──────────────────────────────────────────────────────

def _short_title(text: str, limit: int = 80) -> str:
    """Truncate a summary to a short, human-scannable page title."""
    text = (text or '').strip().replace('\n', ' ')
    if len(text) <= limit:
        return text or 'Untitled'
    cut = text[:limit].rsplit(' ', 1)[0]  # avoid cutting mid-word when possible
    if len(cut) < limit * 0.6:  # word boundary too far back — hard cut instead
        cut = text[:limit]
    return cut.rstrip('.,;: ') + '…'


def _git_info(repo_root: Optional[Path] = None) -> tuple:
    """Cheap best-effort `git branch` + short commit. Returns ('', '') on any
    failure (detached HEAD, not a repo, git missing, timeout) — never raises.
    """
    import subprocess
    root = str(repo_root or Path(__file__).resolve().parent.parent)
    try:
        branch = subprocess.run(
            ['git', 'rev-parse', '--abbrev-ref', 'HEAD'],
            cwd=root, capture_output=True, text=True, timeout=3,
        ).stdout.strip()
        commit = subprocess.run(
            ['git', 'rev-parse', '--short', 'HEAD'],
            cwd=root, capture_output=True, text=True, timeout=3,
        ).stdout.strip()
        return (branch, commit)
    except Exception:
        return ('', '')


def build_vault_body_blocks(
    summary: str,
    *,
    intent_score: Optional[float] = None,
    expert_score: Optional[float] = None,
    adversarial_score: Optional[float] = None,
    factual_score: Optional[float] = None,
    composite_score: Optional[float] = None,
    verdict: str = '',
    expert: str = '',
    skill: str = '',
    workflow: str = '',
    entry_type: str = '',
    task_type: str = '',
    sub_agents: Optional[int] = None,
    session_date: str = '',
    notes: str = '',
    git_branch: str = '',
    git_commit: str = '',
) -> list:
    """Compose the human-readable page body for a Knowledge Vault entry.

    Layout: H2 What was produced -> H2 Scores -> H2 Context -> H2 Notes
    -> H2 Links. Any section with no data is omitted entirely rather than
    printed empty.
    """
    blocks: list = [
        NotionAPI.heading2("What was produced"),
        NotionAPI.para(summary or '(no summary provided)'),
    ]

    score_lines = []
    if intent_score is not None:
        score_lines.append(f"Intent Alignment: {intent_score}/10")
    if expert_score is not None:
        score_lines.append(f"Expert Standard: {expert_score}/10")
    if adversarial_score is not None:
        score_lines.append(f"Adversarial Resilience: {adversarial_score}/10")
    if factual_score is not None:
        score_lines.append(f"Factual Grounding: {factual_score}/10")
    elif any(s is not None for s in (intent_score, expert_score, adversarial_score)):
        score_lines.append("Factual Grounding: N/A")
    if composite_score is not None:
        score_lines.append(f"Composite: {composite_score}/10")
    if verdict:
        score_lines.append(f"Verdict: {verdict}")
    if score_lines:
        blocks.append(NotionAPI.heading2("Scores"))
        blocks.extend(NotionAPI.bullet(line) for line in score_lines)

    ctx_lines = []
    if expert:
        ctx_lines.append(f"Expert: {expert}")
    if skill:
        ctx_lines.append(f"Skill: {skill}")
    if workflow:
        ctx_lines.append(f"Workflow: {workflow}")
    if entry_type:
        ctx_lines.append(f"Type: {entry_type}")
    if task_type:
        ctx_lines.append(f"Task Type: {task_type}")
    if sub_agents is not None:
        ctx_lines.append(f"Sub-agents spawned: {sub_agents}")
    if session_date:
        ctx_lines.append(f"Session Date: {session_date}")
    if ctx_lines:
        blocks.append(NotionAPI.heading2("Context"))
        blocks.extend(NotionAPI.bullet(line) for line in ctx_lines)

    if notes:
        blocks.append(NotionAPI.heading2("Notes"))
        blocks.append(NotionAPI.para(notes))

    if git_branch or git_commit:
        blocks.append(NotionAPI.heading2("Links"))
        link_bits = []
        if git_branch:
            link_bits.append(f"Branch: {git_branch}")
        if git_commit:
            link_bits.append(f"Commit: {git_commit}")
        blocks.append(NotionAPI.para("  |  ".join(link_bits)))

    return blocks


def main():
    parser = argparse.ArgumentParser(description='Notion API CLI')
    sub = parser.add_subparsers(dest='command')

    # query
    q = sub.add_parser('query', help='Query a database')
    q.add_argument('database', help='Database name (projects/knowledge/content/captures/personal) or ID')
    q.add_argument('--limit', type=int, default=10)

    # search
    s = sub.add_parser('search', help='Search Notion')
    s.add_argument('query', help='Search query')
    s.add_argument('--limit', type=int, default=10)

    # capture
    c = sub.add_parser('capture', help='Quick capture')
    c.add_argument('title', help='Capture title')
    c.add_argument('content', help='Raw content')
    c.add_argument('--type', default='Note', help='Type (Idea/Task/Note/Observation/Question)')
    c.add_argument('--tags', default='', help='Comma-separated tags')

    # vault-create
    vc = sub.add_parser('vault-create', help='Create Knowledge Vault entry')
    vc.add_argument('title', help='Entry title')
    vc.add_argument('--source', default='Claude Code', help='Source (default: Claude Code)')
    vc.add_argument('--expert', default='', help='Expert name')
    vc.add_argument('--domain', default='', help='Knowledge domain')
    vc.add_argument('--type', default='Research Brief',
                    choices=['MES 3.0 Extraction', 'Research Brief', 'Framework',
                             'Case Study', 'Pattern Library', 'Book Notes'],
                    help='Entry type (default: Research Brief)')
    vc.add_argument('--patterns', default='', help='Comma-separated key patterns')
    vc.add_argument('--genius-score', type=int, default=None, help='Genius score 2-5')
    vc.add_argument('--date', default=None, help='Date extracted (ISO, default: today)')
    vc.add_argument('--skill', default='', help='Antigravity skill path')
    vc.add_argument('--tags', default='', help='Comma-separated tags (Crown Jewel, Hidden Knowledge, Actionable, Reference)')

    # session-memory
    sm = sub.add_parser('session-memory',
                        help='Push a distilled session-memory row to Notion (allow-listed; no raw transcripts)')
    sm.add_argument('title', help='Session title')
    sm.add_argument('--decisions', required=True, help='Key decisions (distilled — never raw transcript)')
    sm.add_argument('--pickup', default='', help='Pickup prompt to resume in a new session')
    sm.add_argument('--mode', default='Claude Code', help='Advisor/Mode label')
    sm.add_argument('--date', default=None, help='ISO date (default: today)')

    # schema
    sc = sub.add_parser('schema', help='Show database schema')
    sc.add_argument('database', help='Database name or ID')

    args = parser.parse_args()
    api = NotionAPI()

    if args.command == 'query':
        db_id = DB_IDS.get(args.database, args.database)
        result = api.query_database(db_id, page_size=args.limit)
        for page in result.get('results', []):
            title = 'Untitled'
            for prop in page.get('properties', {}).values():
                if prop.get('type') == 'title' and prop.get('title'):
                    title = prop['title'][0]['plain_text'] if prop['title'] else 'Untitled'
                    break
            print(f"  {title} — {page['url']}")

    elif args.command == 'search':
        result = api.search(args.query, args.limit)
        for item in result.get('results', []):
            title = 'Untitled'
            if item['object'] == 'page' and 'properties' in item:
                for prop in item['properties'].values():
                    if prop.get('type') == 'title' and prop.get('title'):
                        title = prop['title'][0]['plain_text'] if prop['title'] else 'Untitled'
                        break
            elif item['object'] == 'database' and item.get('title'):
                title = item['title'][0]['plain_text']
            print(f"  [{item['object']}] {title} — {item.get('url', 'no url')}")

    elif args.command == 'capture':
        tags = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else None
        result = api.capture(args.title, args.content, args.type, tags=tags)
        print(f"  Captured: {result['url']}")

    elif args.command == 'vault-create':
        tags = [t.strip() for t in args.tags.split(',') if t.strip()] if args.tags else None
        try:
            url = api.create_knowledge_vault_entry(
                name=args.title,
                source=args.source,
                expert=args.expert,
                domain=args.domain,
                entry_type=args.type,
                key_patterns=args.patterns,
                genius_score=args.genius_score,
                date_extracted=args.date,
                antigravity_skill=args.skill,
                tags=tags,
            )
            print(f"  Created: {url}")
        except (ValueError, RuntimeError) as e:
            print(f"  Error: {e}")

    elif args.command == 'session-memory':
        try:
            url = api.push_session_memory(
                args.title, args.decisions, pickup_prompt=args.pickup,
                mode=args.mode, date_str=args.date,
            )
            print(f"  Session memory pushed: {url}")
        except (RuntimeError, NotionAPIError) as e:
            print(f"  Error: {e}")

    elif args.command == 'schema':
        db_id = DB_IDS.get(args.database, args.database)
        result = api.get_database(db_id)
        print(f"\n  {result.get('title', [{}])[0].get('plain_text', 'Untitled')}")
        for name, prop in result.get('properties', {}).items():
            detail = ''
            if prop['type'] == 'select' and prop.get('select', {}).get('options'):
                detail = ' [' + ', '.join(o['name'] for o in prop['select']['options']) + ']'
            elif prop['type'] == 'multi_select' and prop.get('multi_select', {}).get('options'):
                detail = ' [' + ', '.join(o['name'] for o in prop['multi_select']['options']) + ']'
            print(f"    {name}: {prop['type']}{detail}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
