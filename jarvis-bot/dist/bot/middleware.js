import { config } from '../config.js';
// 1. Authorization Middleware -> Only Farrice can use Jarvis
export async function authMiddleware(ctx, next) {
    const userId = ctx.from?.id;
    // Bypass if not configured (for initial local dev) but warn loudly
    if (!config.farriceTelegramId) {
        console.warn(`⚠️ authMiddleware: FARRICE_TELEGRAM_ID not set. Permitting request from ${userId}.`);
        await next();
        return;
    }
    if (userId !== config.farriceTelegramId) {
        console.warn(`🛑 Unauthorized access attempt from user ID: ${userId}`);
        await ctx.reply("System restricted. You are not authorized to interact with this AI.");
        return;
    }
    await next();
}
// 2. Logging Middleware
export async function loggerMiddleware(ctx, next) {
    const start = Date.now();
    await next();
    const ms = Date.now() - start;
    console.log(`[Jarvis] Handled update ${ctx.update.update_id} in ${ms}ms`);
}
