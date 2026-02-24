import { GoogleGenAI } from '@google/genai';
import { config } from '../config.js';
import { db } from '../db/store.js';
const activeSessions = new Map();
export function getFlywheelSession(userId) {
    return activeSessions.get(userId);
}
export function startFlywheelSession(userId, rawEntry) {
    activeSessions.set(userId, { state: 'IDLE', rawEntry });
}
export function updateFlywheelSession(userId, session) {
    activeSessions.set(userId, session);
}
export function clearFlywheelSession(userId) {
    activeSessions.delete(userId);
}
const aiClient = new GoogleGenAI({ apiKey: config.geminiApiKey });
async function generate(systemInstruction, prompt) {
    const response = await aiClient.models.generateContent({
        model: 'gemini-2.5-flash',
        contents: prompt,
        config: { systemInstruction }
    });
    return response.text?.trim() || "Simulation failed.";
}
// Prompts based on daily-flywheel.md
const PROMPTS = {
    step1: `You are the Interrogation Chamber (channeling Dan Koe & Jun Yuh).
1. Identify the Core Philosophy: What is the deepest belief or truth hidden in this raw thought?
2. Execute the 'Value Flip': How does this selfless reflection solve a broader audience problem?
Output beautifully formatted Markdown. End by asking the user to confirm if this extraction hits the core truth (Yes/No or structural feedback).`,
    step2: `You are Jim O'Shaughnessy in the Sparring Arena.
Challenge the Truth extracted in the previous step. Point out blind spots, historical parallels, and expand the intellectual frontier. Push for depth. End with 1-2 piercing questions for the user to answer before moving to frameworking.`,
    step3: `You are Kallaway (Deep Ideation & Framework Architecture).
Take the sparred truth and architect it into 2-3 psychologically weaponized "Ideation Concepts" or "Mental Models". Present these 3 distinct frameworks to the user and ask them to choose ONE by replying with 1, 2, or 3.`,
    step4_5: `You are Shaan Puri, Erica Mallet, Ward Farnsworth, and Mitch Albom acting in concert.
The user chose a framework. Generate 3 Masterful Variations of a LinkedIn post based on that framework. 
For each variation:
1. Provide the Post Content.
2. Provide a Masterclass Debrief: The Theme, Expert Reasoning (Why these words/rhetoric?), and Coaching Insights.
End by asking the user which variation they want to finalize (1, 2, or 3).`,
    step7: `You are Nate B Jones running the Zero-Trust Workflow Audit.
Audit the final chosen content for logical breaks, template slop, and hallucinations. Provide 'Zero-Trust Approval' or necessary corrections. If approved, state the final asset is ready for deployment.`
};
export async function processFlywheelInput(userId, text) {
    const session = getFlywheelSession(userId);
    if (!session)
        return "No active flywheel session.";
    try {
        if (session.state === 'IDLE') {
            session.state = 'AWAITING_STEP1_CONFIRM';
            const res = await generate(PROMPTS.step1, `Raw Journal:\n"${session.rawEntry}"`);
            session.extractedTruth = res;
            updateFlywheelSession(userId, session);
            return res;
        }
        if (session.state === 'AWAITING_STEP1_CONFIRM') {
            const isConfirmed = text.toLowerCase().includes('yes') || text.toLowerCase().includes('looks good') || text.toLowerCase().includes('confirm') || text.toLowerCase() === 'y';
            if (!isConfirmed) {
                // User gave feedback, re-run step 1 with feedback
                const res = await generate(PROMPTS.step1, `Raw Journal:\n"${session.rawEntry}"\n\nUser Feedback (Incorporate this):\n"${text}"`);
                session.extractedTruth = res;
                updateFlywheelSession(userId, session);
                return "🔄 Re-interrogating based on feedback...\n\n" + res;
            }
            session.state = 'SPARRING';
            const res = await generate(PROMPTS.step2, `Extracted Truth: ${session.extractedTruth}`);
            updateFlywheelSession(userId, session);
            return "✅ Truth Locked. Entering The Sparring Arena...\n\n" + res;
        }
        if (session.state === 'SPARRING') {
            session.sparringFeedback = text;
            session.state = 'SELECTING_FRAMEWORK';
            const res = await generate(PROMPTS.step3, `Extracted Truth: ${session.extractedTruth}\n\nUser's Sparring Responses: ${session.sparringFeedback}`);
            updateFlywheelSession(userId, session);
            return "🧠 Sparring Complete. Architecting Mental Models...\n\n" + res;
        }
        if (session.state === 'SELECTING_FRAMEWORK') {
            session.chosenFramework = text;
            session.state = 'SELECTING_VARIATION';
            const res = await generate(PROMPTS.step4_5, `Extracted Truth: ${session.extractedTruth}\n\nChosen Framework/Direction: ${session.chosenFramework}`);
            updateFlywheelSession(userId, session);
            return "✍️ Synthesizing & Polishing... (Shaan, Erica, Ward & Mitch are working)\n\n" + res;
        }
        if (session.state === 'SELECTING_VARIATION') {
            session.finalContent = text;
            session.state = 'AUDIT_PENDING';
            const res = await generate(PROMPTS.step7, `Final Chosen Content / Request: ${session.finalContent}\n\nAudit this for structural validity.`);
            // Save to DB
            await db.query('INSERT INTO flywheel_entries (raw_input, processed_output, status) VALUES ($1, $2, $3)', [session.rawEntry, res, 'completed']);
            clearFlywheelSession(userId);
            return "🛡️ Nate B Jones Zero-Trust Audit:\n\n" + res + "\n\n🏁 **Flywheel Engine Cycle Complete. Asset Saved.**";
        }
        return "Unknown state.";
    }
    catch (err) {
        clearFlywheelSession(userId);
        return `⚠️ Flywheel Error: ${err.message}\nSession destroyed.`;
    }
}
