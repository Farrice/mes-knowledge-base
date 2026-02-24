import { CommandContext, Context } from 'grammy';
import { getUnreadInbox } from '../../integrations/gmail.js';

export async function inboxCommand(ctx: CommandContext<Context>) {
    await ctx.reply("⏳ Triaging your inbox...", { parse_mode: 'Markdown' });
    const inbox = await getUnreadInbox();
    await ctx.reply(inbox, { parse_mode: 'Markdown' });
}
