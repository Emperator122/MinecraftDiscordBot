from discord.ext import commands
from comands_handlers.ServerCommandHandlers import ServerCommandHandlers
from comands_handlers.HelpCommandHandlers import HelpCommandHandlers


@commands.command()
async def server(ctx: commands.context.Context, arg):
    try:
        if arg == 'start':
            await ServerCommandHandlers.start(ctx)
        elif arg == 'stop':
            await ServerCommandHandlers.stop(ctx)
        elif arg == 'status':
            await ServerCommandHandlers.status(ctx)
        elif arg == 'sleep':
            await ServerCommandHandlers.sleep(ctx)

    except Exception as e:
        await ctx.send("Произошла ошибка:\n" + str(e))


@commands.command()
async def help(ctx: commands.context.Context):
    await HelpCommandHandlers.show_help(ctx)
