import discord
from discord.ext import commands
from discord.commands import slash_command, Option

class ChangeActivity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @slash_command()
    async def activity(self,ctx, typ: Option(str, choices=["game", "stream"]), name: Option(str)):
        if typ == 'game':
            act = discord.Game(name=name)
        if typ == 'stream':
            act = discord.Streaming(name=name, url='https://www.twitch.tv/iitztimmy')
        await self.bot.change_presence(activity=act, status= discord.Status.online)
        await ctx.respond('Status wurde geändert', ephemeral=True)


def setup(bot):
    bot.add_cog(ChangeActivity(bot))