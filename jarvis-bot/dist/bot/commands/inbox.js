import { getUnreadInbox } from '../../integrations/gmail.js';
export async function inboxCommand(ctx) {
    await ctx.reply("⏳ Triaging your inbox...", { parse_mode: 'Markdown' });
    const query = ctx.match || undefined;
    const inbox = await getUnreadInbox(query);
    await ctx.reply(inbox, { parse_mode: 'Markdown' });
}
