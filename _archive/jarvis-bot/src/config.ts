import * as dotenv from 'dotenv';
import * as path from 'path';

dotenv.config();

export const config = {
    // Telegram
    botToken: process.env.BOT_TOKEN || '',
    telegramWebhookUrl: process.env.TELEGRAM_WEBHOOK_URL || '',
    farriceTelegramId: parseInt(process.env.FARRICE_TELEGRAM_ID || '0', 10),

    // Antigravity Bridge (the core)
    antigravityRoot: process.env.ANTIGRAVITY_ROOT || path.resolve(process.cwd(), '..'),
    claudeModel: process.env.CLAUDE_MODEL || 'claude-sonnet-4-5-20250929',

    // Voice (optional)
    groqApiKey: process.env.GROQ_API_KEY || '',

    // Legacy (kept for backward compat, not required for bridge mode)
    googleClientId: process.env.GOOGLE_CLIENT_ID || '',
    googleClientSecret: process.env.GOOGLE_CLIENT_SECRET || '',
    googleRedirectUri: process.env.GOOGLE_REDIRECT_URI || '',
    geminiApiKey: process.env.GEMINI_API_KEY || '',
    notionApiKey: process.env.NOTION_API_KEY || '',
    databaseUrl: process.env.DATABASE_URL || '',

    // Notion Databases
    notionDbs: {
        projects: process.env.NOTION_DB_PROJECTS || '',
        knowledge: process.env.NOTION_DB_KNOWLEDGE || '',
        content: process.env.NOTION_DB_CONTENT || '',
        captures: process.env.NOTION_DB_CAPTURES || '',
        personal: process.env.NOTION_DB_PERSONAL || '',
    },
};

// Validate critical config on startup
if (!config.botToken) {
    console.warn('BOT_TOKEN is missing. Telegram bot will not start.');
}
if (!config.farriceTelegramId) {
    console.warn('FARRICE_TELEGRAM_ID is missing. Bot will not be restricted.');
}
console.log(`Antigravity root: ${config.antigravityRoot}`);
console.log(`Claude model: ${config.claudeModel}`);
