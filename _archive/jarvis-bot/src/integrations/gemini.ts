import { GoogleGenAI, Type } from '@google/genai';
import { config } from '../config.js';

let aiClient: GoogleGenAI | null = null;

export interface IntentResponse {
    command: '/flywheel' | '/research' | '/capture' | '/goals' | '/status' | '/inbox' | '/cal' | '/expert' | 'unknown';
    arguments: string;
    confidence: number;
}

const intentPrompt = `You are the intent classification engine for Jarvis V2, an elite AI Chief of Staff.
Your job is to analyze the user's free-text natural language message and map it to one of the exact deterministic slash commands the system supports.

AVAILABLE COMMANDS:
/flywheel - Run an idea, thought, or draft through the Daily Flywheel content engine.
/research - Perform deep agentic research on a topic, competitor, or market.
/capture - Quick capture of a thought, note, or task to the database (use as fallback if unsure).
/goals - Viewing, setting, or checking current goals.
/status - Checking system health or status.
/inbox - Check, search, or triage emails from Gmail. Put any specific search filters or topics in the arguments (e.g. "from:amazon", or "bills").
/cal - Add, read, or manage events on Google Calendar.
/expert - Use an Antigravity Expert Skill (like writing copy, analyzing a strategy, etc). Pass the request as arguments.

RULES:
1. Map the user's intent to the single most appropriate command.
2. If the user provides details, include them in the 'arguments' field.
3. If the user asks for help writing, brainstorming, or strategizing using specific frameworks or experts, route to /expert.
4. If the intent is completely ambiguous or conversational, default to 'unknown' or '/capture' if it looks like a note.
5. Respond ONLY with the requested JSON structure.`;

export async function classifyIntent(text: string): Promise<IntentResponse> {
    if (!config.geminiApiKey) {
        console.warn('GEMINI_API_KEY is missing. Defaulting to /capture.');
        return { command: '/capture', arguments: text, confidence: 0 };
    }

    if (!aiClient) {
        aiClient = new GoogleGenAI({ apiKey: config.geminiApiKey });
    }

    try {
        const response = await aiClient.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: text,
            config: {
                systemInstruction: intentPrompt,
                responseMimeType: 'application/json',
                responseSchema: {
                    type: Type.OBJECT,
                    properties: {
                        command: {
                            type: Type.STRING,
                            description: 'The exact slash command including the slash (e.g. /cal, /flywheel, /capture)',
                        },
                        arguments: {
                            type: Type.STRING,
                            description: 'The remaining details or arguments extracted from the user message, or an empty string.',
                        },
                        confidence: {
                            type: Type.NUMBER,
                            description: 'A confidence score from 0.0 to 1.0 that this classification is correct.',
                        }
                    },
                    required: ['command', 'arguments', 'confidence']
                }
            }
        });

        const jsonString = response.text || '{}';
        const parsed = JSON.parse(jsonString) as IntentResponse;
        return parsed;

    } catch (error) {
        console.error('Gemini Classification Error:', error);
        // Fallback to capture on error
        return { command: '/capture', arguments: text, confidence: 0 };
    }
}

import { JARVIS_SYSTEM_PROMPT } from '../prompts/system.js';

export async function generateChatResponse(text: string): Promise<string> {
    if (!config.geminiApiKey) {
        return "I'm currently offline (API key missing).";
    }

    if (!aiClient) {
        aiClient = new GoogleGenAI({ apiKey: config.geminiApiKey });
    }

    try {
        const response = await aiClient.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: text,
            config: {
                systemInstruction: JARVIS_SYSTEM_PROMPT,
            }
        });

        return response.text || "I didn't quite catch that.";
    } catch (error: any) {
        console.error('Gemini Chat Error:', error);
        return `I ran into an issue connecting to my core processing unit: ${error.message}`;
    }
}

export async function transcribeAudio(base64Audio: string, mimeType: string): Promise<string> {
    if (!config.geminiApiKey) {
        throw new Error("GEMINI_API_KEY is missing.");
    }

    if (!aiClient) {
        aiClient = new GoogleGenAI({ apiKey: config.geminiApiKey });
    }

    try {
        const response = await aiClient.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: [
                {
                    role: 'user',
                    parts: [
                        {
                            inlineData: {
                                data: base64Audio,
                                mimeType: mimeType
                            }
                        },
                        { text: 'Please transcribe this audio exactly as spoken. Output ONLY the transcription and nothing else. No markdown wrapping.' }
                    ]
                }
            ]
        });

        return response.text?.trim() || "";
    } catch (error: any) {
        console.error('Gemini Transcription Error:', error);
        throw error;
    }
}
