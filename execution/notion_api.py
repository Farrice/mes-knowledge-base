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
    'projects':  os.getenv('NOTION_DB_PROJECTS', ''),
    'knowledge': os.getenv('NOTION_DB_KNOWLEDGE', ''),
    'content':   os.getenv('NOTION_DB_CONTENT', ''),
    'captures':  os.getenv('NOTION_DB_CAPTURES', ''),
    'personal':  os.getenv('NOTION_DB_PERSONAL', ''),
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
