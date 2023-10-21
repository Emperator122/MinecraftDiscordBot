from typing import List

import discord
from discord.ext import commands
import discord.app_commands as app_commands
from comands_handlers.ServerCommandHandlers import ServerCommandHandlers
from comands_handlers.HelpCommandHandlers import HelpCommandHandlers


async def mc_server_action_autocomplete(
        interaction: discord.Interaction,
        current: str,
) -> List[app_commands.Choice[str]]:
    actions = ['start', 'stop', 'sleep', 'status', 'players_count']
    return [
        app_commands.Choice(name=action, value=action)
        for action in actions if current.lower() in action.lower()
    ]


@commands.hybrid_command(name='server', with_app_command=True,
                         description='Команды, связанные с управлением сервером: включение, выключение, статус, сон, '
                                     'количество игроков')
@app_commands.autocomplete(action=mc_server_action_autocomplete)
async def server(ctx: commands.context.Context, action: str):
    try:
        if action == 'start':
            await ServerCommandHandlers.start(ctx)
        elif action == 'stop':
            await ServerCommandHandlers.stop(ctx)
        elif action == 'status':
            await ServerCommandHandlers.status(ctx)
        elif action == 'sleep':
            await ServerCommandHandlers.sleep(ctx)
        elif action == 'players_count':
            await ServerCommandHandlers.players_count(ctx)
    except Exception as e:
        await ctx.send("Произошла ошибка:\n" + str(e))


@commands.hybrid_command(name='sleep', with_app_command=True, description='Делает утро на сервере')
async def sleep(ctx: commands.context.Context):
    try:
        await ServerCommandHandlers.sleep(ctx)
    except Exception as e:
        await ctx.send("Произошла ошибка:\n" + str(e))


@commands.hybrid_command(name='help', with_app_command=True, description='Список основных команд')
async def help(ctx: commands.context.Context):
    await HelpCommandHandlers.show_help(ctx)
