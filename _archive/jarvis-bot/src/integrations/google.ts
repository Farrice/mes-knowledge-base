import { google } from 'googleapis';
import { config } from '../config.js';
import { db } from '../db/store.js';

export const USER_OAUTH_ID = 'farrice_google_oauth';

// Define the required scopes for Calendar and Gmail
const SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.send'
];

export function getOAuth2Client() {
    return new google.auth.OAuth2(
        config.googleClientId,
        config.googleClientSecret,
        config.googleRedirectUri
    );
}

export function getAuthUrl(): string {
    const oauth2Client = getOAuth2Client();
    return oauth2Client.generateAuthUrl({
        access_type: 'offline', // Requires offline access to get a refresh token
        scope: SCOPES,
        prompt: 'consent' // Force to get refresh token every time asked
    });
}

export async function authorizeWithCode(code: string): Promise<boolean> {
    const oauth2Client = getOAuth2Client();
    try {
        const { tokens } = await oauth2Client.getToken(code);
        oauth2Client.setCredentials(tokens);

        // Calculate expiry date if not provided (assume 1 hour)
        const expiryDate = tokens.expiry_date || (new Date().getTime() + 3600 * 1000);

        // Store tokens in DB
        // upsert basically
        await db.query(`
            INSERT INTO oauth_tokens (id, access_token, refresh_token, expiry_date)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (id) DO UPDATE SET
                access_token = EXCLUDED.access_token,
                refresh_token = COALESCE(EXCLUDED.refresh_token, oauth_tokens.refresh_token),
                expiry_date = EXCLUDED.expiry_date,
                updated_at = CURRENT_TIMESTAMP
        `, [USER_OAUTH_ID, tokens.access_token, tokens.refresh_token || null, expiryDate]);

        return true;
    } catch (err) {
        console.error('Error authorizing Google Code:', err);
        return false;
    }
}

export async function getAuthenticatedClient() {
    const oauth2Client = getOAuth2Client();

    // Get tokens from DB
    const res = await db.query('SELECT access_token, refresh_token, expiry_date FROM oauth_tokens WHERE id = $1', [USER_OAUTH_ID]);

    if (res.rowCount === 0) {
        throw new Error('No Google OAuth tokens found. User needs to authenticate first.');
    }

    const tokenData = res.rows[0];

    oauth2Client.setCredentials({
        access_token: tokenData.access_token,
        refresh_token: tokenData.refresh_token,
        expiry_date: parseInt(tokenData.expiry_date, 10)
    });

    // Check if token needs refresh
    oauth2Client.on('tokens', async (tokens) => {
        if (tokens.refresh_token) {
            console.log('Got new refresh token from Google OAuth Event');
        }
        console.log('Got new access token from Google OAuth Event');
        // Update DB
        const expiryDate = tokens.expiry_date || (new Date().getTime() + 3600 * 1000);
        await db.query(`
            UPDATE oauth_tokens 
            SET access_token = $1, 
                refresh_token = COALESCE($2, refresh_token),
                expiry_date = $3,
                updated_at = CURRENT_TIMESTAMP
            WHERE id = $4
        `, [tokens.access_token, tokens.refresh_token || null, expiryDate, USER_OAUTH_ID]);
    });

    return oauth2Client;
}
