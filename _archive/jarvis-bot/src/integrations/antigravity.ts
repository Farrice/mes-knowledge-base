import * as fs from 'fs/promises';
import * as path from 'path';
import { exec } from 'child_process';
import { promisify } from 'util';
import { config } from '../config.js';

const execAsync = promisify(exec);

// Assuming jarvis-bot is a subfolder in the main Antigravity repo
// In production, we might need an env var to specify the root
const ANTIGRAVITY_ROOT = process.env.ANTIGRAVITY_ROOT || path.resolve(process.cwd(), '..');

/**
 * Ensures the given path is within the Antigravity root to prevent path traversal
 */
function getSafePath(relativePath: string): string {
    const safePath = path.resolve(ANTIGRAVITY_ROOT, relativePath);
    if (!safePath.startsWith(ANTIGRAVITY_ROOT)) {
        throw new Error('Path traversal detected');
    }
    return safePath;
}

export async function listSkills(): Promise<string[]> {
    const skillsPath = getSafePath('skills');
    try {
        const entries = await fs.readdir(skillsPath, { withFileTypes: true });
        return entries
            .filter(entry => entry.isDirectory())
            .map(entry => entry.name);
    } catch (error) {
        console.error('Error reading skills directory:', error);
        return [];
    }
}

export async function listAgents(): Promise<string[]> {
    const agentsPath = getSafePath('agents');
    try {
        const entries = await fs.readdir(agentsPath, { withFileTypes: true });
        return entries
            .filter(entry => entry.isDirectory())
            .map(entry => entry.name);
    } catch (error) {
        console.error('Error reading agents directory:', error);
        return [];
    }
}

export async function listDirectives(): Promise<string[]> {
    const directivesPath = getSafePath('directives');
    try {
        const entries = await fs.readdir(directivesPath, { withFileTypes: true });
        return entries
            .filter(entry => entry.isFile() && entry.name.endsWith('.md'))
            .map(entry => entry.name);
    } catch (error) {
        console.error('Error reading directives directory:', error);
        return [];
    }
}

export async function readDoc(relativePath: string): Promise<string> {
    try {
        const safePath = getSafePath(relativePath);
        return await fs.readFile(safePath, 'utf-8');
    } catch (error: any) {
        console.error(`Error reading doc ${relativePath}:`, error);
        throw new Error(`Failed to read document: ${error.message}`);
    }
}

export async function executePythonScript(scriptName: string, args: string[] = []): Promise<string> {
    try {
        const scriptPath = getSafePath(path.join('execution', scriptName));

        // Basic security check: ensure it's a python file inside execution folder
        if (!scriptPath.endsWith('.py')) {
            throw new Error('Can only execute Python scripts');
        }

        // Sanitize arguments (extremely basic, parameterize properly in production)
        const sanitizedArgs = args.map(arg => `"${arg.replace(/"/g, '\\"')}"`).join(' ');

        const { stdout, stderr } = await execAsync(`python3 "${scriptPath}" ${sanitizedArgs}`, {
            cwd: ANTIGRAVITY_ROOT
        });

        if (stderr) {
            console.warn(`Script stderr for ${scriptName}:`, stderr);
        }

        return stdout;
    } catch (error: any) {
        console.error(`Error executing script ${scriptName}:`, error);
        throw new Error(`Execution failed: ${error.message}`);
    }
}
