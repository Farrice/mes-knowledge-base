import { setupStartCommand } from './start.js';
import { setupCaptureCommand } from './capture.js';
import { expertCommand } from './expert.js';
import { authCommand } from './auth.js';
import { calendarCommand } from './calendar.js';
import { inboxCommand } from './inbox.js';
import { briefingCommand } from './briefing.js';
import { flywheelCommand } from './flywheel.js';
export function setupCommands(bot) {
    setupStartCommand(bot);
    setupCaptureCommand(bot);
    // Remove specific placeholders so that the bot.on('message:text') fallback from intent.ts
    // catches explicit commands correctly with full Notion Context integration.
    bot.command('expert', expertCommand);
    bot.command('auth', authCommand);
    bot.command('cal', calendarCommand);
    bot.command('inbox', inboxCommand);
    bot.command('briefing', briefingCommand);
    bot.command('flywheel', flywheelCommand);
}
