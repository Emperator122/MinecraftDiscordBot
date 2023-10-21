from config.bot_config import BotConfig
from config.minecraft_server_config import MinecraftServerConfig
from commands import commands as bot_commands
from discord.ext import commands
from modules.my_bot import MyBot
from res.resources import ConsoleMessagesString
from discord import Intents, app_commands, Client
from modules.minecraft_server_logger import MinecraftServerLogger


def setup_bot():
    try:
        print(ConsoleMessagesString.launching_message)
        intents = Intents.all()
        bot = MyBot(command_prefix=BotConfig.prefix, intents=intents)

        setup_logger(bot)

        bot.remove_command('help')
        bot.add_command(bot_commands.server)
        bot.add_command(bot_commands.sleep)
        bot.add_command(bot_commands.help)
        bot.run(BotConfig.token)
    except Exception as e:
        print('Ошибка: \r\n' + str(e))


def setup_logger(bot: commands.Bot):
    MinecraftServerLogger.bot = bot


if __name__ == '__main__':
    setup_bot()
