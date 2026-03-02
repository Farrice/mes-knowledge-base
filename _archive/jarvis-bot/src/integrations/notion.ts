/**
 * Notion integration — re-exports from notion-api.ts (the version-pinned wrapper)
 * and provides backward-compatible search/capture functions.
 */

export {
    search as searchNotionRaw,
    capture,
    addKnowledge,
    addPersonalContext,
    addContentIdea,
    addProject,
    createPage,
    updatePage,
    queryDatabase,
    appendBlocks,
    databases,
    prop,
} from './notion-api.js';

import { search, appendBlocks } from './notion-api.js';
import { config } from '../config.js';

/** Search Notion and return a formatted context string */
export async function searchNotion(query: string, limit: number = 5): Promise<string> {
    if (!config.notionApiKey) {
        return "Notion integration is not configured. Please add NOTION_API_KEY to your .env file.";
    }

    try {
        const response = await search(query, limit);

        if (response.results.length === 0) {
            return "No relevant context found in Notion.";
        }

        let contextString = "--- NOTION CONTEXT ---\n";

        for (const page of response.results) {
            let title = "Untitled Page";
            let url = "No URL";
            const type = page.object;

            if (type === 'page') {
                url = page.url || url;
                if (page.properties) {
                    for (const key in page.properties) {
                        if (page.properties[key].type === 'title') {
                            if (page.properties[key].title?.length > 0) {
                                title = page.properties[key].title[0].plain_text;
                            }
                            break;
                        }
                    }
                }
            } else if (type === 'database') {
                url = page.url || url;
                if (page.title?.length > 0) {
                    title = page.title[0].plain_text;
                }
            }

            contextString += `- **${title}** (${type})\n  URL: ${url}\n`;
        }

        contextString += "----------------------\n";
        return contextString;

    } catch (error: any) {
        console.error("Error searching Notion:", error);
        return `Failed to fetch context from Notion: ${error.message}`;
    }
}

/** Append a text block to the Antigravity parent page (backward compat) */
export async function appendCaptureToNotion(content: string): Promise<boolean> {
    if (!config.notionApiKey) return false;

    try {
        const pageId = "21949875a8978036b06bed778786bd61";
        await appendBlocks(pageId, [
            {
                object: 'block',
                type: 'paragraph',
                paragraph: {
                    rich_text: [{ type: 'text', text: { content } }],
                },
            },
        ]);
        return true;
    } catch (error) {
        console.error("Failed to append to Notion:", error);
        return false;
    }
}
