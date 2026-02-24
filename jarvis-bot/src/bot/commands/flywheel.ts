import { CommandContext, Context } from 'grammy';
import { executeFlywheelStep1 } from '../../engine/flywheel.js';

export async function flywheelCommand(ctx: CommandContext<Context>) {
    const rawEntry = ctx.match;

    if (!rawEntry) {
        return ctx.reply("🌪️ **The Daily Flywheel**\nPlease provide your raw journal entry or thought after the command.\nExample: `/flywheel I realized today that...`", { parse_mode: 'Markdown' });
    }

    await ctx.reply("🌪️ **Spinning up the Daily Flywheel Engine...**\n_Ingesting & Interrogating..._", { parse_mode: 'Markdown' });

    try {
        const response = await executeFlywheelStep1(rawEntry);
        await ctx.reply(response, { parse_mode: 'Markdown' });
    } catch (err: any) {
        await ctx.reply(`⚠️ **Flywheel Error:** ${err.message}`, { parse_mode: 'Markdown' });
    }
}
