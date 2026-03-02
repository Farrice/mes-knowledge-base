import { query, type SDKMessage, type Options } from '@anthropic-ai/claude-agent-sdk';
import { getOrCreateSession, updateSessionActivity } from './session-manager.js';
import { injectMemoryContext, storeMessage } from './memory.js';
import { config } from '../config.js';

const ANTIGRAVITY_ROOT = config.antigravityRoot;

interface BridgeResponse {
    text: string;
    sessionId: string;
    costUsd?: number;
    durationMs?: number;
}

/**
 * Bridge a text message to Claude Code via the Agent SDK.
 * This spawns a full Claude Code subprocess with access to all
 * Antigravity skills, agents, MCP servers, and local files.
 */
export async function bridgeToClaudeCode(
    chatId: number,
    userMessage: string,
    mediaContext?: string
): Promise<BridgeResponse> {
    const session = getOrCreateSession(chatId);

    // Build enriched prompt with memory context
    const memoryContext = await injectMemoryContext(chatId, userMessage);

    let enrichedPrompt = userMessage;
    if (mediaContext) {
        enrichedPrompt = `${mediaContext}\n\nUser message: ${userMessage}`;
    }
    if (memoryContext) {
        enrichedPrompt = `[Memory Context]\n${memoryContext}\n\n${enrichedPrompt}`;
    }

    // Build clean env: inherit process.env but strip CLAUDECODE to avoid
    // "cannot be launched inside another Claude Code session" error
    const cleanEnv: Record<string, string | undefined> = { ...process.env };
    delete cleanEnv.CLAUDECODE;

    const sdkOptions: Options = {
        model: config.claudeModel,
        cwd: ANTIGRAVITY_ROOT,
        env: cleanEnv,
        permissionMode: 'bypassPermissions',
        allowDangerouslySkipPermissions: true,
        systemPrompt: {
            type: 'preset',
            preset: 'claude_code',
            append: [
                'You are responding via Telegram to Farrice.',
                'Keep responses concise and mobile-friendly.',
                'Use Markdown formatting (Telegram supports bold, italic, code).',
                'You have full access to the Antigravity system — all skills, agents, directives, and execution scripts.',
                'If the user asks about calendar, email, research, or any Antigravity capability, execute it directly.',
            ].join(' '),
        },
        settingSources: ['project'],
        maxTurns: 25,
        stderr: (data: string) => {
            if (data.trim()) console.error('[Claude SDK stderr]', data.trim());
        },
    };

    // Resume existing session if available
    if (session.claudeSessionId) {
        sdkOptions.resume = session.claudeSessionId;
    }

    let fullResponse = '';
    let newSessionId = session.claudeSessionId || '';
    let costUsd: number | undefined;
    let durationMs: number | undefined;

    const conversation = query({ prompt: enrichedPrompt, options: sdkOptions });

    for await (const message of conversation) {
        // Capture session ID from init
        if (message.type === 'system' && 'subtype' in message && message.subtype === 'init') {
            newSessionId = message.session_id;
            updateSessionActivity(chatId, newSessionId);
        }

        // Accumulate assistant text
        if (message.type === 'assistant' && 'message' in message && message.message?.content) {
            const text = (message.message.content as any[])
                .filter((block: any) => block.type === 'text')
                .map((block: any) => block.text)
                .join('');
            if (text) fullResponse += text;
        }

        // Capture final result
        if (message.type === 'result') {
            if (message.subtype === 'success' && 'result' in message) {
                fullResponse = message.result;
            }
            costUsd = message.total_cost_usd;
            durationMs = message.duration_ms;
        }
    }

    // Store the exchange in memory
    await storeMessage(chatId, 'user', userMessage);
    await storeMessage(chatId, 'assistant', fullResponse);

    return {
        text: fullResponse || 'Done.',
        sessionId: newSessionId,
        costUsd,
        durationMs,
    };
}
