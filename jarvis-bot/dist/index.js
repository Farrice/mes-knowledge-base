import Fastify from 'fastify';
import { Bot, webhookCallback } from 'grammy';
import { config } from './config.js';
import { setupCommands } from './bot/commands/index.js';
import { setupIntentRouter } from './bot/intent.js';
import { authMiddleware, loggerMiddleware } from './bot/middleware.js';
import { setupVoiceHandlers } from './bot/handlers/voice.js';
import { db } from './db/store.js';
import { getAuthUrl, authorizeWithCode } from './integrations/google.js';
import { startSchedulers } from './jobs/scheduler.js';
async function start() {
    const fastify = Fastify({ logger: true });
    const bot = new Bot(config.botToken);
    // Apply basic middleware
    bot.use(loggerMiddleware);
    bot.use(authMiddleware);
    // Setup Commands
    setupCommands(bot);
    // Setup Voice Transcription Handler
    setupVoiceHandlers(bot);
    // Setup Fallback Intent Router
    setupIntentRouter(bot);
    bot.catch((err) => {
        const ctx = err.ctx;
        console.error(`Error while handling update ${ctx.update.update_id}:`);
        console.error(err.error);
    });
    // Webhook route
    // grammY provides a convenient factory for HTTP framework integrations
    if (config.telegramWebhookUrl) {
        fastify.post('/webhook', webhookCallback(bot, 'fastify'));
    }
    // Basic healthcheck
    fastify.get('/health', async () => {
        return { status: 'ok', service: 'jarvis-v2' };
    });
    // Google OAuth Routes
    fastify.get('/oauth', async (request, reply) => {
        const url = getAuthUrl();
        reply.redirect(url);
    });
    fastify.get('/oauth2callback', async (request, reply) => {
        const query = request.query;
        if (query.code) {
            const success = await authorizeWithCode(query.code);
            if (success) {
                return 'Google OAuth Authorization Successful! You can close this window now.';
            }
            else {
                return 'Google OAuth Authorization Failed!';
            }
        }
        return 'No code provided in callback.';
    });
    try {
        const port = parseInt(process.env.PORT || '3000', 10);
        // Initialize Database Schema 
        await db.initSchema();
        // Start Proactive Schedulers
        startSchedulers(bot);
        // Setup Telegram Bot Menu Commands
        await bot.api.setMyCommands([
            { command: 'start', description: 'Start the bot and see commands' },
            { command: 'capture', description: 'Quickly save a note strictly to DB' },
            { command: 'flywheel', description: 'Run the Daily Flywheel' },
            { command: 'research', description: 'Start a deep research task' },
            { command: 'cal', description: 'Manage Calendar events' },
            { command: 'inbox', description: 'Triage Gmail inbox' },
        ]);
        await fastify.listen({ port, host: '0.0.0.0' });
        console.log(`🚀 JARVIS V2 Server listening on port ${port}`);
        // Set Webhook if URL is configured
        if (config.telegramWebhookUrl) {
            await bot.api.setWebhook(`${config.telegramWebhookUrl}/webhook`);
            console.log(`✅ Webhook set to ${config.telegramWebhookUrl}/webhook`);
        }
        else {
            console.warn('⚠️ TELEGRAM_WEBHOOK_URL not set, bot acts in polling mode for local dev.');
            bot.start();
        }
    }
    catch (err) {
        fastify.log.error(err);
        process.exit(1);
    }
}
start();
