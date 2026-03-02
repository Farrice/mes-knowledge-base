import { Bot, Context } from 'grammy';
import * as fs from 'fs/promises';
import { createReadStream } from 'fs';
import * as path from 'path';
import { bridgeToClaudeCode } from '../../claude/agent.js';
import { config } from '../../config.js';

const TEMP_DIR = path.join(config.antigravityRoot, 'jarvis-bot', '.tmp');

export function setupVoiceHandlers(bot: Bot) {
    bot.on(['message:voice', 'message:audio'], async (ctx: Context) => {
        try {
            await ctx.replyWithChatAction('typing');
            const chatId = ctx.chat?.id;
            if (!chatId) return;

            const fileElement = ctx.message?.voice || ctx.message?.audio;
            if (!fileElement) {
                await ctx.reply('Could not find audio data.');
                return;
            }

            const file = await ctx.api.getFile(fileElement.file_id);
            if (!file.file_path) {
                await ctx.reply('Could not get file path from Telegram.');
                return;
            }

            // Download the audio file
            const url = `https://api.telegram.org/file/bot${config.botToken}/${file.file_path}`;
            const response = await fetch(url);
            const buffer = Buffer.from(await response.arrayBuffer());

            await fs.mkdir(TEMP_DIR, { recursive: true });
            const localPath = path.join(TEMP_DIR, `voice-${Date.now()}.ogg`);
            await fs.writeFile(localPath, buffer);

            let transcript: string;

            if (config.groqApiKey) {
                // Transcribe with Groq Whisper
                const Groq = (await import('groq-sdk')).default;
                const groq = new Groq({ apiKey: config.groqApiKey });

                const transcription = await groq.audio.transcriptions.create({
                    file: createReadStream(localPath),
                    model: 'whisper-large-v3',
                });
                transcript = transcription.text;
            } else {
                // Fallback: tell Claude Code about the audio file
                transcript = `[Voice note received, saved at ${localPath}. No transcription API configured.]`;
            }

            if (!transcript.trim()) {
                await ctx.reply('Audio was empty or could not be transcribed.');
                await fs.unlink(localPath).catch(() => {});
                return;
            }

            // Bridge the transcribed text to Claude Code
            const result = await bridgeToClaudeCode(chatId, transcript);

            await ctx.reply(result.text, { parse_mode: 'Markdown' }).catch(() => {
                ctx.reply(result.text);
            });

            // Cleanup
            await fs.unlink(localPath).catch(() => {});
        } catch (error: any) {
            console.error('[Voice] Error:', error.message);
            await ctx.reply('Error processing your voice message.');
        }
    });
}
