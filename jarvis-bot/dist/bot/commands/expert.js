import { listSkills, listAgents, listDirectives } from '../../integrations/antigravity.js';
export async function expertCommand(ctx) {
    try {
        await ctx.replyWithChatAction('typing');
        const skillsTask = listSkills();
        const agentsTask = listAgents();
        const directivesTask = listDirectives();
        const [skills, agents, directives] = await Promise.all([skillsTask, agentsTask, directivesTask]);
        let message = `🧠 <b>Antigravity File System Bridge connected.</b>\n\n`;
        message += `<b>Skills (${skills.length})</b>: ${skills.slice(0, 3).join(', ')}...\n`;
        message += `<b>Agents (${agents.length})</b>: ${agents.slice(0, 3).join(', ')}...\n`;
        message += `<b>Directives (${directives.length})</b>: ${directives.slice(0, 3).join(', ')}...\n\n`;
        message += `<i>(Full execution layer pending. For now, use natural language to request an expert.)</i>`;
        await ctx.reply(message, { parse_mode: "HTML" });
    }
    catch (error) {
        console.error("Antigravity Bridge Error:", error);
        await ctx.reply(`Failed to connect to Antigravity file system: ${error.message}`);
    }
}
