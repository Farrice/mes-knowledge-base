import { getTodayEvents } from '../../integrations/calendar.js';
export async function briefingCommand(ctx) {
    await ctx.reply("🌅 **Good morning, sir. Here is your daily briefing...**\nFetching calendar events...", { parse_mode: 'Markdown' });
    try {
        const calendarText = await getTodayEvents();
        let message = `🌅 **Your Daily Briefing:**\n\n${calendarText}`;
        await ctx.reply(message, { parse_mode: 'Markdown' });
    }
    catch (err) {
        console.error('Error fetching briefing:', err);
        await ctx.reply("⚠️ Encountered an error while preparing your briefing.");
    }
}
