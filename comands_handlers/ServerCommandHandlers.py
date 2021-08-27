from modules.minecraft_server import MinecraftServer
from discord.ext import commands
from config.minecraft_server_config import MinecraftServerConfig as mConfig
from res.resources import BotMessagesStrings


class ServerCommandHandlers:
    minecraft_server = MinecraftServer(mConfig.launch_file_path, mConfig.window_title, mConfig.process_name,
                                       mConfig.cmd_encoding)

    @staticmethod
    async def start(ctx: commands.context.Context):
        if not ServerCommandHandlers._is_launched():
            ServerCommandHandlers.minecraft_server.start_server()
            await ctx.send(BotMessagesStrings.success_launch_message)
        else:
            await ctx.send(BotMessagesStrings.not_success_launch_message)

    @staticmethod
    async def stop(ctx: commands.context.Context):
        if ServerCommandHandlers._is_launched():
            ServerCommandHandlers.minecraft_server.stop_server()
            await ctx.send(BotMessagesStrings.success_stop_message)
        else:
            await ctx.send(BotMessagesStrings.not_success_stop_message)

    @staticmethod
    async def status(ctx: commands.context.Context):
        await ctx.send(BotMessagesStrings.status_on_message if ServerCommandHandlers._is_launched()
                       else BotMessagesStrings.status_off_message)

    @staticmethod
    def _is_launched():
        return ServerCommandHandlers.minecraft_server.is_launched()
