import { Client } from '@notionhq/client';
import { config } from '../config.js';
let notionClient = null;
export function getNotionClient() {
    if (!config.notionApiKey) {
        return null;
    }
    if (!notionClient) {
        notionClient = new Client({ auth: config.notionApiKey });
    }
    return notionClient;
}
export async function searchNotion(query, limit = 5) {
    const notion = getNotionClient();
    if (!notion) {
        return "Notion integration is not configured. Please add NOTION_API_KEY to your .env file.";
    }
    try {
        const response = await notion.search({
            query: query,
            page_size: limit,
            sort: {
                direction: 'descending',
                timestamp: 'last_edited_time',
            },
        });
        if (response.results.length === 0) {
            return "No relevant context found in Notion.";
        }
        let contextString = "--- NOTION CONTEXT ---\n";
        // Very basic extraction of titles/URLs for context to save tokens.
        // Deep reading of page contents would require traversing blocks, which can be slow and token-heavy.
        for (const page of response.results) {
            let title = "Untitled Page";
            let url = "No URL";
            let snippet = "";
            let type = page.object; // 'page' or 'database'
            if (type === 'page') {
                const p = page; // Type casting for simplicity as properties vary widely
                url = p.url || url;
                // Find a property of type 'title'
                if (p.properties) {
                    for (const key in p.properties) {
                        if (p.properties[key].type === 'title') {
                            if (p.properties[key].title && p.properties[key].title.length > 0) {
                                title = p.properties[key].title[0].plain_text;
                            }
                            break;
                        }
                    }
                }
            }
            else if (type === 'database') {
                const db = page;
                url = db.url || url;
                if (db.title && db.title.length > 0) {
                    title = db.title[0].plain_text;
                }
            }
            contextString += `- **${title}** (${type})\n  URL: ${url}\n`;
        }
        contextString += "----------------------\n";
        return contextString;
    }
    catch (error) {
        console.error("Error searching Notion:", error);
        return `Failed to fetch context from Notion: ${error.message}`;
    }
}
export async function appendCaptureToNotion(content) {
    const notion = getNotionClient();
    if (!notion)
        return false;
    try {
        // The page ID provided by the user
        const pageId = "21949875a8978036b06bed778786bd61";
        await notion.blocks.children.append({
            block_id: pageId,
            children: [
                {
                    object: 'block',
                    type: 'paragraph',
                    paragraph: {
                        rich_text: [
                            {
                                type: 'text',
                                text: {
                                    content: content,
                                },
                            },
                        ],
                    },
                },
            ],
        });
        return true;
    }
    catch (error) {
        console.error("Failed to append to Notion:", error);
        return false;
    }
}
