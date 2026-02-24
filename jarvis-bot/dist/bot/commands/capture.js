import { db } from '../../db/store.js';
import { appendCaptureToNotion } from '../../integrations/notion.js';
export function setupCaptureCommand(bot) {
    bot.command('capture', async (ctx) => {
        const text = ctx.match;
        if (!text) {
            return ctx.reply('Please provide text to capture. Example: /capture Read the new article on AI.');
        }
        try {
            await db.query('INSERT INTO captures (content) VALUES ($1)', [text]);
            const notionSuccess = await appendCaptureToNotion(text);
            let message = `✅ Captured successfully:\n"${text}"`;
            if (notionSuccess) {
                message += `\n📝 Added to Notion Teamspace Home.`;
            }
            else {
                message += `\n⚠️ Saved to local DB, but failed adding to Notion.`;
            }
            ctx.reply(message);
        }
        catch (error) {
            console.error('Error capturing text:', error);
            ctx.reply('Failed to save capture to database.');
        }
    });
}
