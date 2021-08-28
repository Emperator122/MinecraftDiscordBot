from config.bot_config import BotConfig
from commands import commands as bot_commands
from discord.ext import commands
from res.resources import ConsoleMessagesString


try:
    print(ConsoleMessagesString.launching_message)
    bot = commands.Bot(command_prefix=BotConfig.prefix)
    bot.remove_command('help')
    bot.add_command(bot_commands.server)
    bot.add_command(bot_commands.help)
    bot.run(BotConfig.token)
except Exception as e:
    print('Ошибка: \r\n'+str(e))

