import Database from 'better-sqlite3';
import path from 'path';
import { config } from '../config.js';

interface Session {
    chatId: number;
    claudeSessionId: string | null;
    startedAt: string;
    lastActive: string;
}

const DB_PATH = path.join(config.antigravityRoot, 'jarvis-bot', 'jarvis.db');
let db: Database.Database;

function getDb(): Database.Database {
    if (!db) {
        db = new Database(DB_PATH);
        db.pragma('journal_mode = WAL');
        db.exec(`
            CREATE TABLE IF NOT EXISTS sessions (
                chat_id INTEGER PRIMARY KEY,
                claude_session_id TEXT,
                started_at TEXT DEFAULT (datetime('now')),
                last_active TEXT DEFAULT (datetime('now'))
            );
        `);
    }
    return db;
}

export function getOrCreateSession(chatId: number): Session {
    const d = getDb();
    let row = d.prepare('SELECT * FROM sessions WHERE chat_id = ?').get(chatId) as any;

    if (!row) {
        d.prepare(
            'INSERT INTO sessions (chat_id) VALUES (?)'
        ).run(chatId);
        row = d.prepare('SELECT * FROM sessions WHERE chat_id = ?').get(chatId) as any;
    }

    return {
        chatId: row.chat_id,
        claudeSessionId: row.claude_session_id,
        startedAt: row.started_at,
        lastActive: row.last_active,
    };
}

export function updateSessionActivity(chatId: number, claudeSessionId: string): void {
    const d = getDb();
    d.prepare(
        'UPDATE sessions SET claude_session_id = ?, last_active = datetime(\'now\') WHERE chat_id = ?'
    ).run(claudeSessionId, chatId);
}

export function clearSession(chatId: number): void {
    const d = getDb();
    d.prepare('UPDATE sessions SET claude_session_id = NULL WHERE chat_id = ?').run(chatId);
}
