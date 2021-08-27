from config.bot_config import BotConfig
from commands import commands as bot_commands
from discord.ext import commands

bot = commands.Bot(command_prefix=BotConfig.prefix)
bot.add_command(bot_commands.server)
bot.run(BotConfig.token)

