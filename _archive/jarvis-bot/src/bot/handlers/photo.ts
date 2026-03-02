import { Bot, Context } from 'grammy';
import * as fs from 'fs/promises';
import * as path from 'path';
import { bridgeToClaudeCode } from '../../claude/agent.js';
import { config } from '../../config.js';

const TEMP_DIR = path.join(config.antigravityRoot, 'jarvis-bot', '.tmp');

export function setupPhotoHandlers(bot: Bot) {
    bot.on('message:photo', async (ctx: Context) => {
        try {
            await ctx.replyWithChatAction('typing');
            const chatId = ctx.chat?.id;
            if (!chatId) return;

            const photos = ctx.message?.photo;
            if (!photos || photos.length === 0) return;

            // Get highest resolution
            const photo = photos[photos.length - 1];
            const file = await ctx.api.getFile(photo.file_id);

            if (!file.file_path) {
                await ctx.reply('Could not get file from Telegram.');
                return;
            }

            // Download the image
            const url = `https://api.telegram.org/file/bot${config.botToken}/${file.file_path}`;
            const response = await fetch(url);
            const buffer = Buffer.from(await response.arrayBuffer());

            // Save to temp directory
            await fs.mkdir(TEMP_DIR, { recursive: true });
            const localPath = path.join(TEMP_DIR, `photo-${Date.now()}.jpg`);
            await fs.writeFile(localPath, buffer);

            // Bridge to Claude Code with image context
            const caption = ctx.message?.caption || 'Analyze this image';
            const mediaContext = `The user sent a photo saved at: ${localPath}`;

            const result = await bridgeToClaudeCode(chatId, caption, mediaContext);

            await ctx.reply(result.text, { parse_mode: 'Markdown' }).catch(() => {
                ctx.reply(result.text);
            });

            // Cleanup
            await fs.unlink(localPath).catch(() => {});
        } catch (error: any) {
            console.error('[Photo] Error:', error.message);
            await ctx.reply('Error processing your photo.');
        }
    });
}
