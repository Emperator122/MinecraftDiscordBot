from modules.minecraft_server import MinecraftServer
from discord.ext import commands
from config.minecraft_server_config import MinecraftServerConfig as mConfig
from res.resources import BotMessagesStrings


class ServerCommandHandlers:
    minecraft_server = MinecraftServer(mConfig.launch_file_path)

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
        ServerCommandHandlers.minecraft_server.execute_command('time set day')
        await ctx.send(BotMessagesStrings.sleep_message)
