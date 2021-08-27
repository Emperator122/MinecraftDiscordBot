import discord
from discord.ext import commands
from res.resources import BotMessagesStrings
from res.resources import BotMessagesStyles


class HelpCommandHandlers:
    @staticmethod
    async def show_help(ctx: commands.context.Context):
        embed = discord.Embed(color=BotMessagesStyles.help_color, title=BotMessagesStrings.help_title)
        for k, v in BotMessagesStrings.help_commands_list.items():
            embed.add_field(name=k, value=v, inline=False)
        await ctx.send(embed=embed)
