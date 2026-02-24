import { searchNotion } from '../integrations/notion.js';
import { config } from '../config.js';
/**
 * Context Bridge
 * Intercepts intent processing before routing to the LLM to provide organizational context.
 *
 * @param query The user's original message
 * @param required Whether context is absolutely necessary (defaults to false)
 * @returns A structured string containing the relevant context
 */
export async function getContextForQuery(query, required = false) {
    if (!config.notionApiKey) {
        if (required) {
            return "WARNING: Context was requested but the Notion API key is not configured.";
        }
        return ""; // Silently fail if context is optional but not configured
    }
    // Optimization: we could use an LLM to extract keywords from the query before searching,
    // but a direct search is much faster. 
    // E.g. query = "Can you help me post about my AI coaching?" -> Notion search might be fuzzy but works okay.
    // For now, doing a raw search:
    const context = await searchNotion(query, 5);
    // If it returns standard error messages or 'No relevant context', format nicely or return empty
    if (context.startsWith("No relevant context") && !required) {
        return "";
    }
    if (context.startsWith("Failed to fetch") || context.startsWith("Notion integration")) {
        console.warn(context);
        return "";
    }
    return `\n\nI have retrieved the following context from the user's Notion workspace. Use this to grounding your response:\n${context}`;
}
