import { Pool } from 'pg';
import { config } from '../config.js';
class Database {
    pool;
    static instance;
    constructor() {
        this.pool = new Pool({
            connectionString: config.databaseUrl,
            // Railway specific connection defaults for stability
            max: 20,
            idleTimeoutMillis: 30000,
            connectionTimeoutMillis: 2000,
        });
        this.pool.on('error', (err) => {
            console.error('Unexpected error on idle pg client', err);
            // Don't exit the process here, let the pool try to reconnect
        });
    }
    static getInstance() {
        if (!Database.instance) {
            Database.instance = new Database();
        }
        return Database.instance;
    }
    async query(text, params) {
        const start = Date.now();
        const res = await this.pool.query(text, params);
        const duration = Date.now() - start;
        console.log(`[DB] Executed query`, { text, duration, rows: res.rowCount });
        return res;
    }
    async initSchema() {
        console.log('[DB] Initializing schema...');
        try {
            // Table for storing captured thoughts/notes
            await this.query(`
                CREATE TABLE IF NOT EXISTS captures (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            `);
            // Table for storing Google OAuth tokens
            await this.query(`
                CREATE TABLE IF NOT EXISTS oauth_tokens (
                    id VARCHAR(255) PRIMARY KEY,
                    access_token TEXT NOT NULL,
                    refresh_token TEXT,
                    expiry_date BIGINT NOT NULL,
                    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            `);
            // Table for Flywheel entries
            await this.query(`
                CREATE TABLE IF NOT EXISTS flywheel_entries (
                    id SERIAL PRIMARY KEY,
                    raw_input TEXT NOT NULL,
                    processed_output TEXT,
                    status VARCHAR(50) DEFAULT 'pending',
                    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
                );
            `);
            console.log('[DB] Schema initialization complete.');
        }
        catch (error) {
            console.error('[DB] Failed to initialize schema:', error);
            throw error;
        }
    }
}
export const db = Database.getInstance();
