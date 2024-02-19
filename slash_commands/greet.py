import discord
from discord.ext import commands
from discord.commands import slash_command

class Greet(commands.Cog):
    def __init__(self, bot:discord.Bot):
        self.bot = bot
    @slash_command()
    async def greet(self,ctx:commands.Context):
        await ctx.respond(f'Hey {ctx.author.mention}')


def setup(bot:discord.Bot):
    bot.add_cog(Greet(bot))