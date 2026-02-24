export function setupStartCommand(bot) {
    bot.command('start', (ctx) => {
        ctx.reply('Hello! Jarvis V2 is online.\n\nAvailable commands:\n/flywheel - Run ideas through the Daily Flywheel\n/research - Deep research on a topic\n/capture - Quick capture notes to DB\n/goals - View current goals\n/status - Check system status\n/inbox - Triage top 5 emails\n/cal - View or add calendar events');
    });
}
