import cron from 'node-cron';
import { config } from '../config.js';
import { getTodayEvents } from '../integrations/calendar.js';
export function startSchedulers(bot) {
    console.log('🕒 Starting proactive schedulers...');
    // Morning Briefing: Runs at 8:00 AM every day
    // Format: '0 8 * * *'
    cron.schedule('0 8 * * *', async () => {
        try {
            console.log('🌅 Running morning briefing job...');
            // Get today's events from the calendar
            const calendarText = await getTodayEvents();
            let message = `🌅 **Good morning, sir. Here is your daily briefing.**\n\n`;
            message += calendarText;
            // Proactive checking - maybe suggesting deep work blocks if there are gaps
            // but for now, just sending the calendar
            await bot.api.sendMessage(config.farriceTelegramId, message, {
                parse_mode: 'Markdown'
            });
            console.log('✅ Morning briefing sent to Farrice.');
        }
        catch (error) {
            console.error('❌ Error executing morning briefing job:', error);
        }
    });
    // We can add more specific proactive checks here in the future
    // E.g., meeting reminders 10 mins before, evening wrap-up, etc.
}
