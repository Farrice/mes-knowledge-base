import { Bot } from 'grammy';
import { config } from '../../config.js';
import { setupCommands } from '../commands/index.js';
import { authMiddleware, loggerMiddleware } from '../middleware.js';

console.log('Starting Test Bot...');
const bot = new Bot(config.botToken);

bot.use(loggerMiddleware);
bot.use(authMiddleware);

setupCommands(bot);

bot.catch((err) => {
    console.error('Error:', err);
});

bot.start({
    onStart: (botInfo) => {
        console.log(`Bot testing online as @${botInfo.username}`);
    }
});
