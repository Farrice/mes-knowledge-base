import { Bot, Context } from 'grammy';
import { bridgeToClaudeCode } from '../claude/agent.js';
import { clearSession } from '../claude/session-manager.js';

const MAX_TELEGRAM_LENGTH = 4000;

/**
 * Process any text message by bridging it directly to Claude Code.
 * Claude Code has access to the full Antigravity system and handles
 * all intent classification, routing, and execution natively.
 */
export async function processTextMessage(ctx: Context, text: string) {
    const chatId = ctx.chat?.id;
    if (!chatId) return;

    // Handle /new command locally (reset session)
    if (text === '/new') {
        clearSession(chatId);
        await ctx.reply('Session cleared. Starting fresh.');
        return;
    }

    await ctx.replyWithChatAction('typing');

    try {
        const response = await bridgeToClaudeCode(chatId, text);

        // Send response, chunking if needed for Telegram's limit
        if (response.text.length <= MAX_TELEGRAM_LENGTH) {
            await ctx.reply(response.text, { parse_mode: 'Markdown' }).catch(() => {
                // Fallback: send without markdown if parsing fails
                ctx.reply(response.text);
            });
        } else {
            for (let i = 0; i < response.text.length; i += MAX_TELEGRAM_LENGTH) {
                const chunk = response.text.slice(i, i + MAX_TELEGRAM_LENGTH);
                await ctx.reply(chunk, { parse_mode: 'Markdown' }).catch(() => {
                    ctx.reply(chunk);
                });
            }
        }

        // Log cost if available
        if (response.costUsd) {
            console.log(`[Bridge] Cost: $${response.costUsd.toFixed(4)} | Duration: ${response.durationMs}ms`);
        }
    } catch (error: any) {
        console.error('[Bridge] Error:', error.message);
        await ctx.reply(`Bridge error: ${error.message}`);
    }
}

export function setupIntentRouter(bot: Bot) {
    bot.on('message:text', async (ctx: Context) => {
        const text = ctx.message?.text;
        if (!text) return;
        await processTextMessage(ctx, text);
    });
}
