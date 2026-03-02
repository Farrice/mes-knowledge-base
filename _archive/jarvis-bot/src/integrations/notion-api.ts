/**
 * Notion API wrapper — uses raw fetch with Notion-Version 2022-06-28.
 *
 * Why not @notionhq/client?
 * v5.9.0 uses a newer API that returns "data_sources" instead of "properties"
 * on databases. Schema updates silently succeed but don't persist, and row
 * inserts fail with "X is not a property that exists." Pinning to 2022-06-28
 * fixes this while keeping full property support.
 */

import { config } from '../config.js';

const NOTION_VERSION = '2022-06-28';
const BASE_URL = 'https://api.notion.com/v1';

function getHeaders(): Record<string, string> {
    return {
        'Authorization': `Bearer ${config.notionApiKey}`,
        'Notion-Version': NOTION_VERSION,
        'Content-Type': 'application/json',
    };
}

export class NotionApiError extends Error {
    status: number;
    code: string;
    constructor(status: number, code: string, message: string) {
        super(message);
        this.name = 'NotionApiError';
        this.status = status;
        this.code = code;
    }
}

async function request(method: string, path: string, body?: unknown): Promise<any> {
    const res = await fetch(`${BASE_URL}${path}`, {
        method,
        headers: getHeaders(),
        body: body ? JSON.stringify(body) : undefined,
    });

    const data: any = await res.json();

    if (!res.ok) {
        throw new NotionApiError(
            res.status,
            data.code || 'unknown',
            data.message || `Notion API ${res.status}`
        );
    }

    return data;
}

// ─── Database Operations ─────────────────────

export async function getDatabase(databaseId: string) {
    return request('GET', `/databases/${databaseId}`);
}

export async function updateDatabaseSchema(databaseId: string, properties: Record<string, any>) {
    return request('PATCH', `/databases/${databaseId}`, { properties });
}

export async function queryDatabase(databaseId: string, filter?: any, sorts?: any[], pageSize = 100) {
    const body: any = { page_size: pageSize };
    if (filter) body.filter = filter;
    if (sorts) body.sorts = sorts;
    return request('POST', `/databases/${databaseId}/query`, body);
}

// ─── Page Operations ─────────────────────────

export async function createPage(databaseId: string, properties: Record<string, any>, children?: any[]) {
    const body: any = {
        parent: { database_id: databaseId },
        properties,
    };
    if (children) body.children = children;
    return request('POST', '/pages', body);
}

export async function updatePage(pageId: string, properties: Record<string, any>) {
    return request('PATCH', `/pages/${pageId}`, { properties });
}

export async function getPage(pageId: string) {
    return request('GET', `/pages/${pageId}`);
}

// ─── Block Operations ────────────────────────

export async function appendBlocks(blockId: string, children: any[]) {
    return request('PATCH', `/blocks/${blockId}/children`, { children });
}

export async function getBlockChildren(blockId: string, pageSize = 100) {
    return request('GET', `/blocks/${blockId}/children?page_size=${pageSize}`);
}

// ─── Search ──────────────────────────────────

export async function search(query: string, pageSize = 10) {
    return request('POST', '/search', {
        query,
        page_size: pageSize,
        sort: { direction: 'descending', timestamp: 'last_edited_time' },
    });
}

// ─── Property Helpers ────────────────────────
// Builders for common Notion property values.

export const prop = {
    title: (text: string) => ({ title: [{ text: { content: text } }] }),
    richText: (text: string) => ({ rich_text: [{ text: { content: text } }] }),
    select: (name: string) => ({ select: { name } }),
    multiSelect: (names: string[]) => ({ multi_select: names.map(name => ({ name })) }),
    number: (value: number) => ({ number: value }),
    date: (start: string, end?: string) => ({ date: { start, ...(end ? { end } : {}) } }),
    checkbox: (checked: boolean) => ({ checkbox: checked }),
    url: (url: string) => ({ url }),
};

// ─── Database ID Shortcuts ───────────────────

export const databases = {
    projects:  config.notionDbs.projects,
    knowledge: config.notionDbs.knowledge,
    content:   config.notionDbs.content,
    captures:  config.notionDbs.captures,
    personal:  config.notionDbs.personal,
};

// ─── High-Level Convenience Functions ────────

/** Quick capture to the Captures database */
export async function capture(name: string, rawContent: string, type: string = 'Note', source: string = 'Claude Code', tags: string[] = []) {
    const today = new Date().toISOString().split('T')[0];
    return createPage(databases.captures, {
        Name:         prop.title(name),
        Type:         prop.select(type),
        Source:       prop.select(source),
        Processed:    prop.checkbox(false),
        'Raw Content': prop.richText(rawContent),
        'Captured At': prop.date(today),
        ...(tags.length ? { Tags: prop.multiSelect(tags) } : {}),
    });
}

/** Add entry to Knowledge Vault */
export async function addKnowledge(name: string, opts: {
    source: string;
    expert?: string;
    domain?: string;
    type?: string;
    keyPatterns: string;
    geniusScore?: number;
    skill?: string;
    tags?: string[];
}) {
    const today = new Date().toISOString().split('T')[0];
    return createPage(databases.knowledge, {
        Name:              prop.title(name),
        Source:            prop.richText(opts.source),
        ...(opts.expert ? { Expert: prop.richText(opts.expert) } : {}),
        ...(opts.domain ? { Domain: prop.richText(opts.domain) } : {}),
        ...(opts.type ? { Type: prop.select(opts.type) } : {}),
        'Key Patterns':   prop.richText(opts.keyPatterns),
        ...(opts.geniusScore ? { 'Genius Score': prop.number(opts.geniusScore) } : {}),
        'Date Extracted': prop.date(today),
        ...(opts.skill ? { 'Antigravity Skill': prop.richText(opts.skill) } : {}),
        ...(opts.tags?.length ? { Tags: prop.multiSelect(opts.tags) } : {}),
    });
}

/** Add entry to Personal Context */
export async function addPersonalContext(name: string, opts: {
    category: string;
    depth: string;
    source: string;
    confidence: string;
    emotions?: string[];
    rawEntry: string;
    extractedInsight: string;
    connectedTo?: string;
    tags?: string[];
}) {
    const today = new Date().toISOString().split('T')[0];
    return createPage(databases.personal, {
        Name:               prop.title(name),
        Category:           prop.select(opts.category),
        Depth:              prop.select(opts.depth),
        Source:             prop.select(opts.source),
        Confidence:         prop.select(opts.confidence),
        ...(opts.emotions?.length ? { Emotion: prop.multiSelect(opts.emotions) } : {}),
        'Raw Entry':        prop.richText(opts.rawEntry),
        'Extracted Insight': prop.richText(opts.extractedInsight),
        ...(opts.connectedTo ? { 'Connected To': prop.richText(opts.connectedTo) } : {}),
        Date:               prop.date(today),
        ...(opts.tags?.length ? { Tags: prop.multiSelect(opts.tags) } : {}),
    });
}

/** Add content idea to Content Pipeline */
export async function addContentIdea(name: string, opts: {
    stage?: string;
    platforms?: string[];
    contentType?: string;
    hook?: string;
    coreIdea?: string;
    expertFramework?: string;
    tags?: string[];
}) {
    return createPage(databases.content, {
        Name:       prop.title(name),
        ...(opts.stage ? { Stage: prop.select(opts.stage) } : {}),
        ...(opts.platforms?.length ? { Platform: prop.multiSelect(opts.platforms) } : {}),
        ...(opts.contentType ? { 'Content Type': prop.richText(opts.contentType) } : {}),
        ...(opts.hook ? { Hook: prop.richText(opts.hook) } : {}),
        ...(opts.coreIdea ? { 'Core Idea': prop.richText(opts.coreIdea) } : {}),
        ...(opts.expertFramework ? { 'Expert Framework Used': prop.richText(opts.expertFramework) } : {}),
        ...(opts.tags?.length ? { Tags: prop.multiSelect(opts.tags) } : {}),
    });
}

/** Add or update project in Projects database */
export async function addProject(name: string, opts: {
    status?: string;
    type?: string;
    priority?: string;
    nextAction?: string;
    description?: string;
    tags?: string[];
}) {
    const today = new Date().toISOString().split('T')[0];
    return createPage(databases.projects, {
        Name:       prop.title(name),
        ...(opts.status ? { Status: prop.select(opts.status) } : {}),
        ...(opts.type ? { Type: prop.select(opts.type) } : {}),
        ...(opts.priority ? { Priority: prop.select(opts.priority) } : {}),
        ...(opts.nextAction ? { 'Next Action': prop.richText(opts.nextAction) } : {}),
        ...(opts.description ? { Description: prop.richText(opts.description) } : {}),
        Started:    prop.date(today),
        ...(opts.tags?.length ? { Tags: prop.multiSelect(opts.tags) } : {}),
    });
}
