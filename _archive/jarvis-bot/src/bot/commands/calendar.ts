import { CommandContext, Context } from 'grammy';
import { getTodayEvents } from '../../integrations/calendar.js';

export async function calendarCommand(ctx: CommandContext<Context>) {
    await ctx.reply("⏳ Fetching your calendar...", { parse_mode: 'Markdown' });
    const events = await getTodayEvents();
    await ctx.reply(events, { parse_mode: 'Markdown' });
}
