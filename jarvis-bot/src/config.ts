import * as dotenv from 'dotenv';

dotenv.config();

export const config = {
    botToken: process.env.BOT_TOKEN || '',
    telegramWebhookUrl: process.env.TELEGRAM_WEBHOOK_URL || '',
    farriceTelegramId: parseInt(process.env.FARRICE_TELEGRAM_ID || '0', 10),
    googleClientId: process.env.GOOGLE_CLIENT_ID || '',
    googleClientSecret: process.env.GOOGLE_CLIENT_SECRET || '',
    googleRedirectUri: process.env.GOOGLE_REDIRECT_URI || '',
    databaseUrl: process.env.DATABASE_URL || '',
    geminiApiKey: process.env.GEMINI_API_KEY || '',
    notionApiKey: process.env.NOTION_API_KEY || '',
};

// Validate critical config on startup
if (!config.botToken) {
    console.warn('⚠️ BOT_TOKEN is missing. Telegram bot will not start correctly.');
}
if (!config.farriceTelegramId) {
    console.warn('⚠️ FARRICE_TELEGRAM_ID is missing. Security risk: Bot will not be restricted.');
}
