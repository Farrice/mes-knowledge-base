import { google } from 'googleapis';
import { getAuthenticatedClient } from './google.js';
/**
 * Get the events for today from the primary calendar
 */
export async function getTodayEvents() {
    try {
        const auth = await getAuthenticatedClient();
        const calendar = google.calendar({ version: 'v3', auth });
        // Calculate time min and max for today
        const now = new Date();
        const startOfDay = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 0, 0, 0);
        const endOfDay = new Date(now.getFullYear(), now.getMonth(), now.getDate(), 23, 59, 59);
        const res = await calendar.events.list({
            calendarId: 'primary',
            timeMin: startOfDay.toISOString(),
            timeMax: endOfDay.toISOString(),
            maxResults: 10,
            singleEvents: true,
            orderBy: 'startTime',
        });
        const events = res.data.items;
        if (!events || events.length === 0) {
            return `📅 No upcoming events found for today.`;
        }
        let eventList = `📅 **Today's Schedule:**\n\n`;
        events.forEach((event, i) => {
            let start = event.start?.dateTime || event.start?.date;
            // Format time nicely if it's a dateTime
            let timeString = start;
            if (event.start?.dateTime) {
                const date = new Date(event.start.dateTime);
                timeString = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            }
            else if (event.start?.date) {
                timeString = "(All Day)";
            }
            eventList += `${i + 1}. **${event.summary}** ⁃ ${timeString}\n`;
        });
        return eventList;
    }
    catch (error) {
        console.error('The API returned an error: ' + error);
        if (error.message && error.message.includes('No Google OAuth tokens found')) {
            return "⚠️ I couldn't access your Calendar. Please run /auth to connect your Google account.";
        }
        return `⚠️ Encountered an error fetching calendar events.`;
    }
}
