import { Bot } from 'grammy';
import { config } from './config.js';
import { setupIntentRouter } from './bot/intent.js';
import { authMiddleware, loggerMiddleware } from './bot/middleware.js';
import { setupVoiceHandlers } from './bot/handlers/voice.js';
import { setupPhotoHandlers } from './bot/handlers/photo.js';
import { clearSession } from './claude/session-manager.js';

async function start() {
    const bot = new Bot(config.botToken);

    // Middleware: logging + auth (only Farrice)
    bot.use(loggerMiddleware);
    bot.use(authMiddleware);

    // /start command
    bot.command('start', async (ctx) => {
        await ctx.reply([
            'Antigravity Bridge Active.',
            '',
            'Send any message — text, voice, photo — and it goes directly to your Claude Code instance with full access to all skills, agents, and tools.',
            '',
            'Commands:',
            '/new — Start a fresh session',
            '/start — Show this message',
        ].join('\n'));
    });

    // /new command — clear session
    bot.command('new', async (ctx) => {
        if (ctx.chat?.id) clearSession(ctx.chat.id);
        await ctx.reply('Session cleared. Next message starts fresh.');
    });

    // Media handlers (voice, photos) — before the text fallback
    setupVoiceHandlers(bot);
    setupPhotoHandlers(bot);

    // Text handler — bridges everything to Claude Code
    setupIntentRouter(bot);

    bot.catch((err) => {
        console.error(`[Bot] Error handling update ${err.ctx.update.update_id}:`, err.error);
    });

    // Set Telegram menu commands
    await bot.api.setMyCommands([
        { command: 'start', description: 'Show help' },
        { command: 'new', description: 'Start a fresh session' },
    ]);

    // Start in polling mode (simplest for local use)
    console.log('Antigravity Bridge starting...');
    console.log(`Root: ${config.antigravityRoot}`);
    console.log(`Model: ${config.claudeModel}`);

    bot.start();
    console.log('Bridge active. Listening for Telegram messages.');
}

start().catch((err) => {
    console.error('Fatal:', err);
    process.exit(1);
});
