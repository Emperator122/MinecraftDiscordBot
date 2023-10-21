from config.minecraft_server_config import MinecraftServerConfig as mConfig
from models.extract_log_data_dto import ExtractLogDataTask
from models.minecraft_server_responce import MinecraftPlayersCountCommandResponse
from modules.minecraft_server import MinecraftServer
from discord.ext import commands

from modules.my_bot import MyBot
from res.resources import BotMessagesStrings
from modules.minecraft_server_logger import MinecraftServerLogger


class ServerCommandHandlers:
    minecraft_server = MinecraftServer(mConfig.launch_file_path,
                                       on_console_log_message=MinecraftServerLogger.on_console_log_message)

    @staticmethod
    async def start(ctx: commands.context.Context):
        ServerCommandHandlers.minecraft_server.start_server()
        await ctx.send(BotMessagesStrings.success_launch_message)

    @staticmethod
    async def stop(ctx: commands.context.Context):
        await ctx.send(BotMessagesStrings.stopping_message)
        ServerCommandHandlers.minecraft_server.stop_server()
        await ctx.send(BotMessagesStrings.success_stop_message)

    @staticmethod
    async def status(ctx: commands.context.Context):
        await ctx.send(BotMessagesStrings.status_on_message if ServerCommandHandlers.minecraft_server.is_launched()
                       else BotMessagesStrings.status_off_message)

    @staticmethod
    async def sleep(ctx: commands.context.Context):
        ServerCommandHandlers.minecraft_server.execute_command('time set 0')
        await ctx.send(BotMessagesStrings.sleep_message)

    @staticmethod
    async def players_count(ctx: commands.context.Context):
        await ctx.send(BotMessagesStrings.task_get_players_count_message)
        MinecraftServerLogger.extract_log_data_task_add(ExtractLogDataTask(ctx.channel.id,
                                                                           MinecraftPlayersCountCommandResponse()))
        ServerCommandHandlers.minecraft_server.execute_command('list')
