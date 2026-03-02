import Database from 'better-sqlite3';
import path from 'path';
import { config } from '../config.js';

const DB_PATH = path.join(config.antigravityRoot, 'jarvis-bot', 'jarvis.db');
let db: Database.Database;

function getDb(): Database.Database {
    if (!db) {
        db = new Database(DB_PATH);
        db.pragma('journal_mode = WAL');
        db.exec(`
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                role TEXT CHECK(role IN ('user', 'assistant')) NOT NULL,
                content TEXT NOT NULL,
                created_at TEXT DEFAULT (datetime('now')),
                weight REAL DEFAULT 1.0
            );

            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chat_id INTEGER NOT NULL,
                type TEXT CHECK(type IN ('semantic', 'episodic')) NOT NULL,
                content TEXT NOT NULL,
                keywords TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                last_accessed TEXT,
                access_count INTEGER DEFAULT 0,
                weight REAL DEFAULT 1.0
            );

            CREATE INDEX IF NOT EXISTS idx_messages_chat ON messages(chat_id, created_at DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_chat ON memories(chat_id, weight DESC);
        `);
    }
    return db;
}

/**
 * Store a message in the conversation history.
 */
export async function storeMessage(
    chatId: number,
    role: 'user' | 'assistant',
    content: string
): Promise<void> {
    if (!content.trim()) return;
    const d = getDb();
    d.prepare(
        'INSERT INTO messages (chat_id, role, content) VALUES (?, ?, ?)'
    ).run(chatId, role, content);
}

/**
 * Inject memory context before each Claude Code invocation.
 * Searches recent messages and top memories, deduplicates, and formats.
 */
export async function injectMemoryContext(
    chatId: number,
    currentMessage: string
): Promise<string> {
    const d = getDb();

    // Layer 1: Recent conversation (last 10 messages for this chat)
    const recentMessages = d.prepare(
        `SELECT role, content, created_at FROM messages
         WHERE chat_id = ?
         ORDER BY created_at DESC
         LIMIT 10`
    ).all(chatId) as any[];

    // Layer 2: Top memories by weight (if any exist)
    const topMemories = d.prepare(
        `SELECT content, type, weight FROM memories
         WHERE chat_id = ?
         ORDER BY weight DESC
         LIMIT 5`
    ).all(chatId) as any[];

    // Build context block
    const parts: string[] = [];

    if (recentMessages.length > 0) {
        const convo = recentMessages
            .reverse()
            .map((m: any) => `${m.role === 'user' ? 'User' : 'Assistant'}: ${truncate(m.content, 200)}`)
            .join('\n');
        parts.push(`Recent conversation:\n${convo}`);
    }

    if (topMemories.length > 0) {
        const mems = topMemories
            .map((m: any) => `- [${m.type}] ${truncate(m.content, 150)}`)
            .join('\n');
        parts.push(`Key memories:\n${mems}`);
    }

    return parts.join('\n\n');
}

/**
 * Store a semantic or episodic memory for long-term recall.
 */
export async function storeMemory(
    chatId: number,
    content: string,
    type: 'semantic' | 'episodic',
    keywords?: string
): Promise<void> {
    const d = getDb();
    d.prepare(
        'INSERT INTO memories (chat_id, type, content, keywords) VALUES (?, ?, ?, ?)'
    ).run(chatId, type, content, keywords || null);
}

/**
 * Decay all memory weights. Run periodically (e.g., daily via cron).
 * Half-life determines how quickly old memories fade.
 */
export function decayWeights(halfLifeDays: number = 7): void {
    const d = getDb();
    const decayFactor = Math.pow(0.5, 1 / halfLifeDays);

    // Decay message weights
    d.prepare('UPDATE messages SET weight = weight * ?').run(decayFactor);

    // Decay memory weights
    d.prepare('UPDATE memories SET weight = weight * ?').run(decayFactor);

    // Clean up very low weight entries (< 0.01)
    d.prepare('DELETE FROM messages WHERE weight < 0.01').run();
}

function truncate(text: string, maxLen: number): string {
    if (text.length <= maxLen) return text;
    return text.slice(0, maxLen) + '...';
}
