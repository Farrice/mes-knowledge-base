import { CommandContext, Context } from 'grammy';
import { getAuthUrl } from '../../integrations/google.js';

export async function authCommand(ctx: CommandContext<Context>) {
    const authUrl = getAuthUrl();
    await ctx.reply(
        `🔐 *Google Integration Setup*\n\nPlease click the link below to authorize JARVIS V2 with your Google account. This gives the bot access to read/write to your Calendar and triage your Gmail:\n\n[Authorize JARVIS](${authUrl})\n\n_Note: You must be on the same network as the server (e.g. localhost) for the redirect to work._`,
        { parse_mode: 'Markdown' }
    );
}
