import { google } from 'googleapis';
import { getAuthenticatedClient } from './google.js';
export async function getUnreadInbox() {
    try {
        const auth = await getAuthenticatedClient();
        const gmail = google.gmail({ version: 'v1', auth });
        const res = await gmail.users.messages.list({
            userId: 'me',
            q: 'is:unread in:inbox',
            maxResults: 10
        });
        const messages = res.data.messages;
        if (!messages || messages.length === 0) {
            return `📭 Your inbox is clear!`;
        }
        let messageList = `📩 **Inbox Triage (${messages.length} unread):**\n\n`;
        // Fetch details for each message
        for (let i = 0; i < messages.length; i++) {
            const msg = messages[i];
            if (msg.id) {
                const detailedMsg = await gmail.users.messages.get({
                    userId: 'me',
                    id: msg.id,
                    format: 'metadata',
                    metadataHeaders: ['Subject', 'From']
                });
                const headers = detailedMsg.data.payload?.headers;
                const subject = headers?.find(h => h.name === 'Subject')?.value || 'No Subject';
                const from = headers?.find(h => h.name === 'From')?.value || 'UnknownSender';
                // Clean up 'from' to just the name or email
                const cleanedFrom = from.replace(/<.*>/, '').trim();
                messageList += `${i + 1}. **${cleanedFrom}** - _${subject}_\n`;
            }
        }
        return messageList;
    }
    catch (error) {
        console.error('The API returned an error: ' + error);
        if (error.message && error.message.includes('No Google OAuth tokens found')) {
            return "⚠️ I couldn't access your Gmail. Please run /auth to connect your Google account.";
        }
        return `⚠️ Encountered an error fetching emails.`;
    }
}
