import { classifyIntent, generateChatResponse } from '../integrations/gemini.js';
import { db } from '../db/store.js';
import { appendCaptureToNotion } from '../integrations/notion.js';
import { executeFlywheelStep1 } from '../engine/flywheel.js';
export async function processTextIntent(ctx, text) {
    let intentCommand = '';
    let intentArgs = '';
    if (text.startsWith('/')) {
        const parts = text.split(' ');
        intentCommand = parts[0];
        intentArgs = parts.slice(1).join(' ');
    }
    else {
        await ctx.replyWithChatAction('typing');
        const intent = await classifyIntent(text);
        console.log(`[Intent Router] Mapped "${text}" -> ${intent.command} (conf: ${intent.confidence})`);
        if (intent.confidence < 0.6 || intent.command === 'unknown') {
            const response = await generateChatResponse(text);
            await ctx.reply(response);
            return;
        }
        intentCommand = intent.command;
        intentArgs = intent.arguments || '';
    }
    switch (intentCommand) {
        case '/capture':
            try {
                const content = intentArgs || text;
                await db.query('INSERT INTO captures (content) VALUES ($1)', [content]);
                const notionSuccess = await appendCaptureToNotion(content);
                let message = `✅ Captured via Intent Routing:\n"${content}"`;
                if (notionSuccess) {
                    message += `\n📝 Added to Notion Teamspace Home.`;
                }
                else {
                    message += `\n⚠️ Saved to local DB, but failed adding to Notion.`;
                }
                await ctx.reply(message);
            }
            catch (error) {
                await ctx.reply('Failed to save capture to database.');
            }
            break;
        case '/cal':
            await ctx.reply(`Got it. You want to manage your calendar: "${intentArgs}".\n(Google Calendar integration pending Phase 2)`);
            break;
        case '/inbox':
            await ctx.reply(`Got it. You want to check your email inbox.\n(Gmail integration pending Phase 2)`);
            break;
        case '/flywheel':
            if (!intentArgs) {
                await ctx.reply("🌪️ Please provide a thought or entry to run through the Flywheel.");
                break;
            }
            await ctx.reply("🌪️ **Spinning up the Daily Flywheel Engine...**\n_Ingesting & Interrogating..._", { parse_mode: 'Markdown' });
            try {
                const flywheelResult = await executeFlywheelStep1(intentArgs);
                await ctx.reply(flywheelResult, { parse_mode: 'Markdown' });
            }
            catch (err) {
                await ctx.reply(`⚠️ **Flywheel Error:** ${err.message}`, { parse_mode: 'Markdown' });
            }
            break;
        case '/research':
            await ctx.reply(`Initiating Agentic Research for:\n"${intentArgs}"\n(Research integration pending)`);
            break;
        case '/expert':
            try {
                const { listSkills } = await import('../integrations/antigravity.js');
                const skills = await listSkills();
                const topSkills = skills.slice(0, 5).join(', ');
                await ctx.reply(`Routing to Antigravity Expert Brain with query:\n"${intentArgs}"\nBridge Status: Connected to local file system. Found ${skills.length} skills (e.g., ${topSkills}).\n(Execution pending)`);
            }
            catch (error) {
                console.error("Antigravity Bridge Error:", error);
                await ctx.reply(`Failed to connect to Antigravity file system: ${error.message}`);
            }
            break;
        case '/goals':
        case '/status':
            await ctx.reply(`Executing ${intentCommand}... (Module pending)`);
            break;
        default:
            await ctx.reply(`I classified your intent as ${intentCommand}, but I don't know how to execute that yet.`);
    }
}
export function setupIntentRouter(bot) {
    bot.on('message:text', async (ctx) => {
        const text = ctx.message?.text;
        if (!text)
            return;
        await processTextIntent(ctx, text);
    });
}
