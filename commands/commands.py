from discord.ext import commands
from comands_handlers.ServerCommandHandlers import ServerCommandHandlers


@commands.command()
async def server(ctx: commands.context.Context, arg):
    try:
        if arg == 'start':
            await ServerCommandHandlers.start(ctx)
        elif arg == 'stop':
            await ServerCommandHandlers.stop(ctx)
        elif arg == 'status':
            await ServerCommandHandlers.status(ctx)

    except Exception as e:
        await ctx.send("Произошла ошибка:\n" + str(e))
