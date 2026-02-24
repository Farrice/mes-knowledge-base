import { GoogleGenAI } from '@google/genai';
import { config } from '../config.js';

const flywheelStep1Prompt = `You are executing STEP 1 of the Antigravity Daily Flywheel Engine.
Role: The Interrogation Chamber (channeling Dan Koe & Jun Yuh).

Your objective is to ingest the user's raw journal entry and perform "The Selfless Translation":
1. Identify the Core Philosophy: What is the deepest belief or truth hidden in this raw thought?
2. Execute the 'Value Flip': How does this selfless reflection solve a broader audience problem?
3. Present the extraction to the user for confirmation.

Format your output beautifully for Telegram (using Markdown).
End your message by asking the user to confirm if this extraction feels accurate and hits the core truth, before moving to Step 2 (The Sparring Arena with Jim O'Shaughnessy).`;

export async function executeFlywheelStep1(rawEntry: string): Promise<string> {
    if (!config.geminiApiKey) {
        throw new Error("GEMINI_API_KEY is missing. Cannot execute Flywheel.");
    }

    const aiClient = new GoogleGenAI({ apiKey: config.geminiApiKey });

    try {
        const response = await aiClient.models.generateContent({
            model: 'gemini-2.5-flash',
            contents: `Raw Journal Entry:\n"${rawEntry}"`,
            config: {
                systemInstruction: flywheelStep1Prompt,
            }
        });

        return response.text?.trim() || "Failed to generate Flywheel extraction.";
    } catch (error: any) {
        console.error('Flywheel Engine Error:', error);
        throw new Error(`Failed to spin the Flywheel: ${error.message}`);
    }
}
