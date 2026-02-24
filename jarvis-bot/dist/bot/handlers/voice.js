import axios from 'axios';
import { transcribeAudio } from '../../integrations/gemini.js';
import { config } from '../../config.js';
import { processTextIntent } from '../intent.js';
export function setupVoiceHandlers(bot) {
    bot.on(['message:voice', 'message:audio'], async (ctx) => {
        try {
            await ctx.reply("🎙️ Processing voice memo...");
            const fileElement = ctx.message?.voice || ctx.message?.audio;
            if (!fileElement) {
                return ctx.reply("⚠️ Could not find audio data.");
            }
            const fileId = fileElement.file_id;
            const file = await ctx.api.getFile(fileId);
            if (!file.file_path) {
                return ctx.reply("⚠️ Could not get file path from Telegram.");
            }
            const url = `https://api.telegram.org/file/bot${config.botToken}/${file.file_path}`;
            // Download the file
            const response = await axios.get(url, { responseType: 'arraybuffer' });
            const buffer = Buffer.from(response.data, 'binary');
            const base64Audio = buffer.toString('base64');
            const mimeType = fileElement.mime_type || 'audio/ogg'; // Telegram voice is usually ogg
            // Ask Gemini to transcribe
            const transcription = await transcribeAudio(base64Audio, mimeType);
            if (!transcription) {
                return ctx.reply("⚠️ Audio was empty or could not be transcribed.");
            }
            await ctx.reply(`🗣️ **Transcription:**\n_${transcription}_`, { parse_mode: 'Markdown' });
            // Now, act like the user typed this transcription
            if (ctx.message) {
                // Mock message object for intent handler
                const mockCtx = Object.create(ctx);
                mockCtx.message = { ...ctx.message, text: transcription };
                await processTextIntent(mockCtx, transcription);
            }
        }
        catch (error) {
            console.error('❌ Error handling voice message:', error);
            await ctx.reply("⚠️ Encountered an error while transcribing your voice memo.");
        }
    });
}
