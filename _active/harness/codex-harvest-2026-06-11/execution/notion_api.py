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
try:
    import bootstrap
except ModuleNotFoundError:
    from execution import bootstrap
import requests
import socket
from pathlib import Path
from typing import Any, Optional
from dotenv import load_dotenv

# Load .env — jarvis-bot first (has Notion keys), then root as fallback
# load_dotenv doesn't override existing vars, so order matters
ENV_PATHS = [
    Path(__file__).parent.parent / 'jarvis-bot' / '.env',
    Path(__file__).parent.parent / '.env',
]
for env_path in ENV_PATHS:
    if env_path.exists():
        load_dotenv(env_path)

NOTION_VERSION = '2022-06-28'
BASE_URL = 'https://api.notion.com/v1'
NOTION_HOST = 'api.notion.com'

# Database IDs from environment, with registry fallbacks from
# directives/notion-databases.md. The env aliases still win when present.
DB_IDS = {
    'projects':  os.getenv('NOTION_DB_PROJECTS', 'cf93599a-a201-4e55-a6b9-f2f58ae6fd77'),
    'knowledge': os.getenv('NOTION_DB_KNOWLEDGE', '5c63b25c-e040-4c6f-8a7b-906643090694'),
    'content':   os.getenv('NOTION_DB_CONTENT', 'ff77ee45-8ee8-4fce-996e-20c76fa65d9c'),
    'captures':  os.getenv('NOTION_DB_CAPTURES', 'f55d202d-233c-4284-a8f1-7ab1c145ffe1'),
    'personal':  os.getenv('NOTION_DB_PERSONAL', '0911ef04-8117-463f-8b21-e7f6c1a1ef4a'),
    'performance': os.getenv('NOTION_DB_PERFORMANCE', '31f49875a89781dbb599dee5e7961b5c'),
}


def check_dns(host: str = NOTION_HOST) -> dict:
    """Return a small DNS status payload without raising on sandbox failures."""
    try:
        socket.getaddrinfo(host, 443)
        return {'status': 'ok', 'host': host, 'error': ''}
    except socket.gaierror as e:
        return {'status': 'network_unavailable', 'host': host, 'error': str(e)}
    except OSError as e:
        return {'status': 'network_unavailable', 'host': host, 'error': str(e)}


def env_status() -> dict:
    """Report required Notion environment aliases without exposing secrets."""
    api_key = (os.getenv('NOTION_API_KEY', '') or '').strip('"').strip("'")
    return {
        'notion_api_key': 'present' if api_key else 'missing',
        'databases': {
            alias: {
                'id': db_id,
                'source': 'env' if os.getenv(f'NOTION_DB_{alias.upper()}') else 'fallback',
            }
            for alias, db_id in DB_IDS.items()
        },
        'env_files': [str(path) for path in ENV_PATHS if path.exists()],
    }


def status_payload(database: str = 'knowledge', limit: int = 1) -> dict:
    """Read-only Notion status check for diagnostics and health reports."""
    env = env_status()
    dns = check_dns()
    payload = {
        'env': env,
        'dns': dns,
        'api': {
            'status': 'not_checked',
            'database': database,
            'results': 0,
            'error': '',
        },
        'recommendation': '',
    }

    if env['notion_api_key'] != 'present':
        payload['api']['status'] = 'missing_key'
        payload['recommendation'] = 'Set NOTION_API_KEY or use local-first evidence until the key is available.'
        return payload

    if dns['status'] != 'ok':
        payload['api']['status'] = 'network_unavailable'
        payload['api']['error'] = dns['error']
        payload['recommendation'] = 'Use local-first evidence or run the Notion check in a network-enabled context.'
        return payload

    try:
        api = NotionAPI()
        db_id = DB_IDS.get(database, database)
        result = api.query_database(db_id, page_size=limit)
        payload['api']['status'] = 'ok'
        payload['api']['database'] = database
        payload['api']['results'] = len(result.get('results', []))
        payload['recommendation'] = 'Notion API reachable. Remote sync/search can run.'
    except Exception as e:
        payload['api']['status'] = 'api_error'
        payload['api']['error'] = str(e)
        payload['recommendation'] = 'Keep local-first evidence and inspect the Notion API error before syncing.'

    return payload


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
        res = requests.request(method, url, headers=self.headers, json=body, timeout=20)
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
    ) -> str:
        """Create an entry in the Knowledge Vault database.

        Args:
            name: Entry title (required).
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

        Returns:
            The Notion page URL of the created entry.
        """
        from datetime import date as _date

        if date_extracted is None:
            date_extracted = _date.today().isoformat()

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

        # Build properties
        props: dict[str, Any] = {
            'Name': self.title(name),
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

        # Knowledge Vault database ID
        vault_db_id = DB_IDS.get('knowledge', '5c63b25c-e040-4c6f-8a7b-906643090694')
        if not vault_db_id:
            vault_db_id = '5c63b25c-e040-4c6f-8a7b-906643090694'

        try:
            result = self.create_page(vault_db_id, props)
            return result['url']
        except NotionAPIError as e:
            raise RuntimeError(
                f"Failed to create Knowledge Vault entry: [{e.status}] {e.code} — {e}"
            ) from e


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

    # schema
    sc = sub.add_parser('schema', help='Show database schema')
    sc.add_argument('database', help='Database name or ID')

    # status
    st = sub.add_parser('status', help='Check Notion env, DNS, and read-only API reachability')
    st.add_argument('--database', default='knowledge', help='Database alias or ID to query (default: knowledge)')
    st.add_argument('--limit', type=int, default=1, help='Read-only query size (default: 1)')
    st.add_argument('--json', action='store_true', help='Print machine-readable JSON')

    args = parser.parse_args()

    if args.command == 'status':
        payload = status_payload(database=args.database, limit=args.limit)
        if args.json:
            print(json.dumps(payload, indent=2))
        else:
            print("Notion Status")
            print(f"  API key:     {payload['env']['notion_api_key']}")
            print(f"  DNS:         {payload['dns']['status']}")
            if payload['dns'].get('error'):
                print(f"  DNS error:   {payload['dns']['error']}")
            print(f"  API:         {payload['api']['status']}")
            print(f"  Database:    {payload['api']['database']}")
            print(f"  Results:     {payload['api']['results']}")
            if payload['api'].get('error'):
                print(f"  API error:   {payload['api']['error']}")
            print(f"  Next:        {payload['recommendation']}")
        return

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
